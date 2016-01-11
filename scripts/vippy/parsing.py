"""
Supports parsing the reST files and generating the initial YAML files.

This module is not needed for updating the reST.
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
    'HtmlColorString': 'html_color_string',
    'LanguageString': 'language_string',
    'LatLng': 'lat_lng',
    'NonHouseAddress': 'non_house_address',
    'Schedule': 'schedule',
    'Term': 'term',
    'TimeWithZone': 'time_with_zone',
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


def make_yaml_path(rel_path, type_name):
    rel_base = fix_rel_path(rel_path, type_name)
    yaml_path = os.path.join(common.YAML_DIR, rel_base + ".yaml")
    return yaml_path


def parse_type(rel_path, type_name, iter_lines, parent_type=None):
    msg = "parsing type: {0}".format(type_name)
    if parent_type is not None:
        msg += " ({0})".format(parent_type)
    _log.debug(msg)

    new_lines = []
    next_type = None
    type_description = None
    for line in iter_lines:
        norm_line = line.replace("\t", "    ").rstrip()
        assert "\t" not in norm_line

        # Check to see if we have reached a "child type."
        assert "===" not in norm_line
        # Checking for a space rules out headers like:
        #   ``Name`` and ``AddressLine`` Usage Note
        if "---" in norm_line and " " not in previous_line:
            next_type = previous_line
            # Remove the header line added in the previous loop iteration.
            new_lines.pop()
            break
        previous_line = norm_line

        if norm_line.startswith(".. include:: ../../tables"):
            # Then we reached the end of the description (aka the "pre").
            type_description = "\n".join(new_lines)
            # Start the "post."
            new_lines = []
        else:
            new_lines.append(norm_line)

    # If we got here, then we have finished reading all lines of a type.
    if type_description is None:
        # Then there is no "post."
        type_description = "\n".join(new_lines)
        type_post = ""
    else:
        type_post = "\n".join(new_lines)

    child_types = []
    # Child types should only be processed by the original (parent) type.
    if next_type is not None and parent_type is None:
        while True:
            child_types.append(next_type)
            next_type = parse_type(rel_path, next_type, iter_lines, parent_type=type_name)
            if next_type is None:
                break

    # Create or update the corresponding YAML file.
    yaml_path = make_yaml_path(rel_path, type_name)
    if os.path.exists(yaml_path):
        yaml_data = common.read_yaml(yaml_path)
        if "name" in yaml_data:
            name = yaml_data['name']
            assert name == type_name
            del yaml_data['name']
    else:
        yaml_data = {}
    yaml_data["_name"] = type_name
    if child_types:
        yaml_data["_sub_types"] = child_types
    type_description = type_description.strip()
    if type_description:
        yaml_data["description"] = type_description
    type_post = type_post.strip()
    if type_post:
        yaml_data["post"] = type_post
    common.write_yaml(yaml_data, yaml_path)

    return next_type


def rest_file_to_yaml(parent_dir, rest_path):
    """
    Parse a reST file, and convert it to use a YAML file.

    This function--

    1) parses a reST file,
    2) extracts all of the information, and then
    3) creates (or updates) one or more YAML files in the correct location.
    """
    dir_name = os.path.basename(os.path.dirname(rest_path))
    if dir_name not in ('elements', 'enumerations'):
        _log.info("skipping: {0}".format(rest_path))
        return

    _log.debug("parsing file: {0}".format(rest_path))
    is_enum = (dir_name == 'enumerations')
    column_infos, cell_values = rest.get_type_info(is_enum)
    rel_path = os.path.relpath(rest_path, start=parent_dir)

    with open(rest_path) as f:
        lines = f.readlines()
    table_number = 0
    iter_lines = iter(lines)

    first_line = next(iter_lines)
    type_name = first_line.strip()
    # Skip past the header marker "=====".
    next(iter_lines)

    parse_type(rel_path, type_name, iter_lines)
