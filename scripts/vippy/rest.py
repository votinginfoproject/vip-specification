# Copyright (c) 2015, Christopher Jerdonek
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the names of the copyright holders nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import itertools
import logging
import os.path
from pprint import pformat, pprint
import textwrap

from vippy import common
from vippy.common import (TAG_KEY_NAME, TAG_KEY_TYPE, TAG_KEY_REQUIRED,
                          TAG_KEY_REPEATING, TAG_KEY_DESCRIPTION,
                          TAG_KEY_ERROR_HANDLE)


_log = logging.getLogger()

MIN_COLUMN_WIDTH = 12

TABLE_COMMENT = """\
.. This file is auto-generated.  Do not edit it by hand!

"""

TYPE_NAME_TO_BASE_NAME = {
    'Department': 'department',
    'ExternalIdentifier': 'external_identifier',
    'Hours': 'hours',
    'LatLng': 'lat_lng',
    'NonHouseAddress': 'non_house_address',
    'Schedule': 'schedule',
    'Term': 'term',
    'VoterService': 'voter_service',
}

ELEMENT_COLUMNS = [
    (TAG_KEY_NAME, 'Tag', MIN_COLUMN_WIDTH),
    (TAG_KEY_TYPE, 'Data Type', MIN_COLUMN_WIDTH),
    (TAG_KEY_REQUIRED, 'Required?', MIN_COLUMN_WIDTH),
    (TAG_KEY_REPEATING, 'Repeats?', MIN_COLUMN_WIDTH),
    (TAG_KEY_DESCRIPTION, 'Description', 40),
    (TAG_KEY_ERROR_HANDLE, 'Error Handling', 40),
]

ENUMERATION_COLUMNS = [
    ('_name', 'Tag', MIN_COLUMN_WIDTH),
    ('description', 'Description', 50),
]


ELEMENT_CELL_VALUES = {
    TAG_KEY_TYPE: common.reverse_map(common.TYPE_MAP),
    TAG_KEY_REQUIRED: {
        False: 'Optional',
        True: '**Required**',
    },
    TAG_KEY_REPEATING: {
        False: 'Single',
        True: 'Repeats',
    },
}

ENUMERATION_CELL_VALUES = {}


def get_type_info(path):
    if 'elements' in path:
        column_infos = ELEMENT_COLUMNS
        cell_values = ELEMENT_CELL_VALUES
    else:
        column_infos = ENUMERATION_COLUMNS
        cell_values = ENUMERATION_CELL_VALUES
    return column_infos, cell_values


def make_table(path):
    data = common.read_yaml(path)
    tags = data['tags']
    formatter = make_table_formatter(path)
    lines = formatter.make_table(tags)
    table = "\n".join(lines) + "\n"

    return table


def update_table_file(parent_dir, yaml_path):
    rel_path = os.path.relpath(yaml_path, start=parent_dir)
    root, ext = os.path.splitext(rel_path)
    rest_rel_path = "{0}.rst".format(root)
    rest_path = os.path.join(common.TABLES_DIR, rest_rel_path)
    table = make_table(yaml_path)
    text = TABLE_COMMENT + table
    common.write(rest_path, text)


def make_table_formatter(path):
    column_infos, cell_values = get_type_info(path)
    keys, headers, widths = ([c[i] for c in column_infos] for i in range(3))
    formatter = TableFormatter(headers=headers, keys=keys, widths=widths, cell_values=cell_values)
    return formatter


def parse_row(iter_lines):
    """Parse the next row of a reST table.

    Returns the values in the next row as a list of strings.
    """
    lines = []
    for line in iter_lines:
        if line.startswith('+--'):
            break
        if not line.startswith('|'):
            return False
        lines.append(line)
    else:
        # Then there are no more lines in the file.
        return False
    parts_seq = []
    for line in lines:
        line = line.strip().strip('|')
        parts = [part.strip() for part in line.split('|')]
        parts_seq.append(parts)
    values = []
    for i in range(len(parts_seq[0])):
        value = " ".join(parts[i] for parts in parts_seq if parts[i])
        values.append(value)
    return values


def values_to_tag_data(values, columns_info):
    data = {}
    for column_info, value in zip(columns_info, values):
        key = column_info[0]
        data[key] = value
    return data


def parse_table(iter_lines, columns_info):
    # Advance past the header row.
    for line in iter_lines:
        if line.startswith('+==='):
            break
    tags_data = []
    while True:
        values = parse_row(iter_lines)
        if values is False:
            break
        if len(values) != len(columns_info):
            raise Exception("{0} != {1}".format(len(values), len(columns_info)))
        tag_data = values_to_tag_data(values, columns_info=columns_info)
        tags_data.append(tag_data)
    return tags_data


def snake_to_camel(text):
    parts = text.split("_")
    return "".join([p.capitalize() for p in parts])


def fix_rel_path(rel_path, type_name):
    root, ext = os.path.splitext(rel_path)
    rel_dir, base_name = os.path.split(root)
    base_name = TYPE_NAME_TO_BASE_NAME.get(type_name, base_name)
    camel_base_name = snake_to_camel(base_name)
    if camel_base_name != type_name:
        raise Exception("{0} != {1}".format(camel_base_name, type_name))
    path = os.path.join(rel_dir, base_name)
    return path


def parse_tables(parent_dir, rest_path):
    _log.info("parsing: {0}".format(rest_path))
    column_infos, cell_values = get_type_info(rest_path)
    rel_path = os.path.relpath(rest_path, start=parent_dir)
    with open(rest_path) as f:
        lines = f.readlines()
    table_number = 0
    iter_lines = iter(lines)
    new_lines = []
    for line in iter_lines:
        norm_line = line.strip()
        if (norm_line and " " not in norm_line and "-" not in norm_line and
            "=" not in norm_line and not norm_line.endswith('.')):
            type_name = norm_line.split(".")[-1]
        if not norm_line.startswith("+---"):
            new_lines.append(line)
            continue
        # Otherwise, we just started a table.
        rel_base = fix_rel_path(rel_path, type_name)
        rel_table_path = rel_base + ".rst"
        yaml_path = os.path.join(common.DATA_DIR, rel_base + ".yaml")
        new_line = ".. include:: ../../tables/{0}\n\n".format(rel_table_path)
        new_lines.append(new_line)
        tags_data = parse_table(iter_lines, column_infos)
        data = {
            'name': type_name,
            'tags': tags_data,
        }
        common.write_yaml(data, yaml_path)
    new_rest = "".join(new_lines)
    common.write(rest_path, new_rest)


def analyze_types():
    dir_path = os.path.join(common.DATA_DIR, 'elements')
    yaml_paths = common.get_all_files(dir_path, ext='.yaml')
    values = {}
    for yaml_path in yaml_paths:
#        _log.info("processing: {0}".format(path))
        formatter = make_table_formatter(yaml_path)
        data = common.read_yaml(yaml_path)
        tags_data = data['tags']
        for tag_data in tags_data:
            tag_type = tag_data[TAG_KEY_TYPE]
            if not TAG_KEY_ERROR_HANDLE in tag_data:
                continue
            error = common.get_tag_value(tag_data, TAG_KEY_ERROR_HANDLE)
            error_if = "If the field is invalid"
            if error.startswith(error_if):
                error_then = error[len(error_if):].strip()
                del tag_data[TAG_KEY_ERROR_HANDLE]
                tag_data[TAG_KEY_ERROR_THEN] = error_then
            else:
                print(error)
        common.write_yaml(data, yaml_path)
    #pprint(values)


class TableFormatter(object):

    # The size of the left and right margin of each cell as a number of spaces.
    margin = 1

    def __init__(self, cell_values, headers, keys, widths):
        self.cell_values = cell_values
        self.headers = headers
        self.keys = keys
        self.min_widths = widths

    def wrap(self, text, width):
        return textwrap.wrap(text, width=width, break_long_words=False,
                             break_on_hyphens=False)

    def get_cell_value(self, tag_data, key):
        data_value = common.get_tag_value(tag_data, key)
        try:
            conversions = self.cell_values[key]
        except KeyError:
            value = data_value
        else:
            value = conversions.get(data_value, data_value)
        if value.startswith('='):
            raise Exception("unconverted value: {0}".format(value))
        return value

    def make_width(self, i, header, tags_data):
        all_words = [header]
        key = self.keys[i]
        for tag_data in tags_data:
            value = self.get_cell_value(tag_data, key)
            words = value.split(" ")
            all_words.extend(words)
        width = max(len(w) for w in all_words)
        width = max(width, self.min_widths[i])
        return width

    def make_widths(self, headers, tags_data):
        widths = []
        for i, header in enumerate(headers):
            width = self.make_width(i, header, tags_data)
            widths.append(width)
        return widths

    def get_cell_widths(self, widths):
        return [w + 2 * self.margin for w in widths]

    def make_line(self, parts, glue):
        parts = [''] + parts + ['']
        line = glue.join(parts)
        return line

    def make_divider(self, widths, fill_char=None):
        if fill_char is None:
            fill_char = '-'
        cell_widths = self.get_cell_widths(widths)
        parts = [w * fill_char for w in cell_widths]
        line = self.make_line(parts, glue='+')
        return line

    def make_text_line(self, parts, widths):
        cell_widths = self.get_cell_widths(widths)
        parts = [(self.margin * " " + s).ljust(w) for s, w in zip(parts, cell_widths)]
        line = self.make_line(parts, glue='|')
        return line

    def make_row(self, cell_values, widths, separator=None):
        if separator is None:
            separator = '-'
        contents = [self.wrap(s, width=w) for s, w in zip(cell_values, widths)]
        parts_seq = itertools.zip_longest(*contents, fillvalue='')
        lines = [self.make_text_line(parts, widths=widths) for parts in parts_seq]
        lines.append(self.make_divider(widths=widths, fill_char=separator))
        return lines

    def make_row_from_data(self, tag_data, widths):
        cell_values = [self.get_cell_value(tag_data, k) for k in self.keys]
        lines = self.make_row(cell_values, widths=widths)
        return lines

    def make_table(self, tags_data):
        widths = self.make_widths(self.headers, tags_data)
        lines = [self.make_divider(widths)]
        lines.extend(self.make_row(self.headers, widths, separator='='))
        for tag_data in tags_data:
            lines.extend(self.make_row_from_data(tag_data, widths=widths))
        return lines
