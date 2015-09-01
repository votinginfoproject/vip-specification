"""
Supports parsing the reST files and generating the initial YAML files.

"""

import os
import logging

from vippy import common
from vippy.common import (TAG_KEY_ERROR_BASE, TAG_KEY_ERROR_HANDLE, TAG_KEY_ERROR_THEN,
                          TAG_KEY_REPEATING, TAG_KEY_REQUIRED, TAG_KEY_TYPE)
from vippy import rest


_log = logging.getLogger(__name__)


XS_TYPES = set(['xs:anyURI', 'xs:boolean', 'xs:dateTime', 'xs:float', 'xs:integer',
                'xs:date', 'xs:string', 'xs:IDREF'])

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

ERROR_THEN_MAP = {
    'If the element is invalid or not present, the implementation is required to ignore it.': '=must-ignore',
    'If the element is invalid or not present, then the implementation is required to ignore it.': '=must-ignore',
    'If the element is invalid or not present, the implementation should ignore it.': '=should-ignore',
    'If the field is invalid or not present, the implementation is required to ignore it.': '=must-ignore',
    'If the field is invalid or not present, the implementation should ignore it.': '=should-ignore',
    'If the field is invalid or not present, then the implementation is required to ignore it.': '=must-ignore',
    'If the field is invalid the implementation is required to ignore it.': '=must-ignore',
    'If the field is invalid, the implementation is required to ignore it.': '=must-ignore',
    'If the field is missing or invalid, the implementation is required to ignore it.': '=must-ignore',
    'If the field is not present or invalid, the implementation is required to ignore it.': '=must-ignore',
    'If the field is not present or invalid, the implementation is required to ignore the element containing it.': '=must-ignore-containing-element',
    'If the field is invalid or not present, the implementation is required to ignore the element containing it.': '=must-ignore-containing-element',
    'If field is invalid or not present, the implementation is required to ignore the element containing it.': '=must-ignore-containing-element',
}

REPEATING_MAP = {
    'Single': None,
    'Repeats': True,
}

REQUIRED_MAP = {
    'Optional': None,
    '**Required**': True,
}

REST_TO_TYPE_NAME = common.reverse_map(rest.TYPE_NAME_TO_REST)


def parsed_value_to_yaml_value(value, info):
    """
    Convert a value parsed from the reST into the value that should
    appear in the YAML file.
    """
    key, header_name, width = info

    if key == TAG_KEY_REPEATING:
        value = REPEATING_MAP[value]
    elif key == TAG_KEY_REQUIRED:
        value = REQUIRED_MAP[value]
    elif key == TAG_KEY_TYPE:
        try:
            value = REST_TO_TYPE_NAME[value]
        except KeyError:
            if not value in XS_TYPES:
                raise
    elif key == TAG_KEY_ERROR_HANDLE:
        try:
            value = ERROR_THEN_MAP[value]
        except KeyError:
            key = TAG_KEY_ERROR_BASE
        else:
            if value == '=must-ignore-containing-element':
                # This case is covered by our default error message generation.
                value = '=must-ignore'
            key = TAG_KEY_ERROR_THEN

    return key, value


def snake_to_camel(text):
    """Convert a string from snake_case to CamelCase."""
    parts = text.split("_")
    camel = "".join([p.capitalize() for p in parts])
    return camel


def fix_rel_path(rel_path, type_name):
    root, ext = os.path.splitext(rel_path)
    rel_dir, base_name = os.path.split(root)
    base_name = TYPE_NAME_TO_BASE_NAME.get(type_name, base_name)
    camel_base_name = snake_to_camel(base_name)
    if camel_base_name != type_name:
        raise Exception("{0} != {1}".format(camel_base_name, type_name))
    path = os.path.join(rel_dir, base_name)
    return path


def parse_row(iter_lines):
    """
    Parse the next row of a reST table.

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
    """
    Returns a dict mapping tag keys to cell values.
    """
    data = {}
    for column_info, value in zip(columns_info, values):
        key = column_info[0]
        key, value = parsed_value_to_yaml_value(value, column_info)
        if value is not None:
            data[key] = value
    return data


def parse_table(iter_lines, columns_info):
    """Parse a single reST table"""
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


def rest_file_to_yaml(parent_dir, rest_path):
    """
    Parse a reST file, and convert it to use a YAML file.

    This function parses a reST file, extracts the table data,
    creates (or updates) one or more YAML files in the correct location,
    and then updates the reST file to use tables generated from the
    YAML files.
    """
    dir_name = os.path.basename(os.path.dirname(rest_path))
    if dir_name not in ('elements', 'enumerations'):
        _log.info("skipping: {0}".format(rest_path))
        return

    _log.debug("parsing: {0}".format(rest_path))
    is_enum = (dir_name == 'enumerations')
    column_infos, cell_values = rest.get_type_info(is_enum)
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
        yaml_path = os.path.join(common.YAML_DIR, rel_base + ".yaml")
        dir_path = os.path.dirname(yaml_path)
        if not os.path.exists(dir_path):
            _log.info("creating dir: {0}".format(dir_path))
            os.makedirs(dir_path)
        new_line = ".. include:: ../../tables/{0}\n\n".format(rel_table_path)
        new_lines.append(new_line)
        tags_data = parse_table(iter_lines, column_infos)
        data = {
            'name': type_name,
            'tags': tags_data,
        }
        common.write_yaml(data, yaml_path)
    new_rest = "".join(new_lines)
    common.write_file(rest_path, new_rest)
