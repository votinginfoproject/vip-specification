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
import os.path
from pprint import pprint
import textwrap

from vippy import common

TABLES_DIR = 'docs/tables'

TABLE_COMMENT = """\
.. This file is auto-generated.  Do not edit it by hand!

"""

# TODO: convert this to COLUMNS.
_HEADERS = ('Tag', 'Data Type', 'Required?', 'Repeats?', 'Description', 'Error Handling')
_KEYS = ('name', 'type', 'required', 'repeating', 'description', 'error')
_WIDTHS = (18, 39, 13, 10, 38, 24)

DEFAULT_VALUES = {
    'required': 'Optional',
    'repeating': 'Single',
}

def make_table(path):
    data = common.read_yaml(path)
    tags = data['tags']
    formatter = make_table_formatter()
    lines = formatter.make_table(tags)
    table = "\n".join(lines) + "\n"

    return table


def update_table_file(yaml_path, tables_dir):
    file_name = os.path.basename(yaml_path)
    root, ext = os.path.splitext(file_name)
    rest_file_name = "{0}.rst".format(root)
    rest_path = os.path.join(tables_dir, rest_file_name)
    table = make_table(yaml_path)
    text = TABLE_COMMENT + table
    common.write(rest_path, text)


def make_table_formatter():
    formatter = TableFormatter(headers=_HEADERS, keys=_KEYS, widths=_WIDTHS)
    return formatter


def make_yaml_path(root, table_number):
    if table_number > 1:
        root += "_{0}".format(table_number)
    path = root + ".yaml"
    path = os.path.join(common.DATA_DIR, path)
    return path


def parse_table(iter_lines):
    for line in lines:
        print(line)


def parse_tables(parent_dir, path):
    rel_path = os.path.relpath(path, start=parent_dir)
    root, ext = os.path.splitext(rel_path)
    output_path = os.path.join(TABLES_DIR, rel_path)
    with open(path) as f:
        lines = f.readlines()
    table_number = 0
    iter_lines = iter(lines)
    for line in iter_lines:
        if "+===" in line:
            # Then we just consumed a table header.
            table_number += 1
            path = make_yaml_path(root, table_number)
            print(path)
            parse_table(iter_lines)


class TableFormatter(object):

    # The size of the left and right margin of each cell as a number of spaces.
    margin = 1

    def __init__(self, headers, keys, widths):
        self.headers = headers
        self.keys = keys
        self.widths = widths

    def make_line(self, parts, glue):
        parts = [''] + parts + ['']
        line = glue.join(parts)
        return line

    def make_divider(self, fill_char=None):
        if fill_char is None:
            fill_char = '-'
        parts = [w * fill_char for w in self.widths]
        line = self.make_line(parts, glue='+')
        return line

    def make_text_line(self, parts):
        parts = [(self.margin * " " + s).ljust(w) for s, w in zip(parts, self.widths)]
        line = self.make_line(parts, glue='|')
        return line

    def make_row(self, strings, separator=None):
        if separator is None:
            separator = '-'
        widths = [w - 2 * self.margin for w in self.widths]
        contents = [textwrap.wrap(s, width=w) for s, w in zip(strings, widths)]
        parts_seq = itertools.zip_longest(*contents, fillvalue='')
        lines = [self.make_text_line(parts) for parts in parts_seq]
        lines.append(self.make_divider(fill_char=separator))
        return lines

    def make_row_from_data(self, data):
        texts = [data.get(k, DEFAULT_VALUES.get(k, '')) for k in self.keys]
        lines = self.make_row(texts)
        return lines

    def make_table(self, tags_data):
        lines = [self.make_divider()]
        lines.extend(self.make_row(self.headers, separator='='))
        for tag_data in tags_data:
            lines.extend(self.make_row_from_data(tag_data))
        return lines
