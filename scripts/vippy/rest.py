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


# A dict mapping type names to how they should appear in the reST.
TYPE_NAME_TO_REST = {
    'BallotMeasureType': ':doc:`BallotMeasureType <../enumerations/ballot_measure_type>`',
    'CandidatePostElectionStatus': ':doc:`CandidatePostElectionStatus <../enumerations/candidate_post_election_status>`',
    'CandidatePreElectionStatus': ':doc:`CandidatePreElectionStatus <../enumerations/candidate_pre_election_status>`',
    'ContactInformation': ':doc:`ContactInformation <contact_information>`',
    'Department': ':ref:`Department <ea-dep>`',
    'DistrictType': ':doc:`DistrictType <../enumerations/district_type>`',
    'ExternalIdentifier': '`ExternalIdentifier`_',
    'ExternalIdentifiers': ':doc:`ExternalIdentifiers <external_identifiers>`',
    'Hours': '`Hours`_',
    'HtmlColorString': '`HtmlColorString`_',
    'IdentifierType': ':doc:`IdentifierType <../enumerations/identifier_type>`',
    'InternationalizedText': ':doc:`InternationalizedText <internationalized_text>`',
    'LanguageString': '`LanguageString`_',
    'LatLng': '`LatLng`_',
    'NonHouseAddress': '`NonHouseAddress`_',
    'OebEnum': ':doc:`OebEnum <../enumerations/oeb_enum>`',
    'OfficeTermType': ':doc:`OfficeTermType <../enumerations/office_term_type>`',
    'Schedule': '`Schedule`_',
    'Term': '`Term`_',
    'TimeWithZone': '`TimeWithZone`_',
    'VoteVariation': ':doc:`VoteVariation <../enumerations/vote_variation>`',
    'VoterService': ':ref:`VoterService <ea-dep-voter-service>`',
    'VoterServiceType': ':doc:`VoterServiceType <../enumerations/voter_service_type>`'
}


# The reST table columns for an element.
ELEMENT_COLUMNS = [
    (TAG_KEY_NAME, 'Tag', MIN_COLUMN_WIDTH),
    (TAG_KEY_TYPE, 'Data Type', MIN_COLUMN_WIDTH),
    (TAG_KEY_REQUIRED, 'Required?', MIN_COLUMN_WIDTH),
    (TAG_KEY_REPEATING, 'Repeats?', MIN_COLUMN_WIDTH),
    (TAG_KEY_DESCRIPTION, 'Description', 40),
    (TAG_KEY_ERROR_HANDLE, 'Error Handling', 40),
]

# The reST table columns for an enumeration.
ENUMERATION_COLUMNS = [
    (TAG_KEY_NAME, 'Tag', MIN_COLUMN_WIDTH),
    (TAG_KEY_DESCRIPTION, 'Description', 50),
]


# A dictionary of "conversions" for table cell values.
# This is useful for converting Python objects and special string
# values to formatted reST strings for human-readability.
# For example, this dictionary converts a Python value of True for the
# "required" column to the formatted reST string "**Required**".
ELEMENT_CELL_VALUES = {
    TAG_KEY_TYPE: TYPE_NAME_TO_REST,
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


def get_type_info(is_enum):
    # Sanity-check to make sure this function is being used correctly.
    assert type(is_enum) == bool
    if is_enum:
        column_infos = ENUMERATION_COLUMNS
        cell_values = ENUMERATION_CELL_VALUES
    else:
        # Otherwise, it is an element.
        column_infos = ELEMENT_COLUMNS
        cell_values = ELEMENT_CELL_VALUES
    return column_infos, cell_values


def make_table_formatter(all_types, data_type):
    is_enum = data_type.is_enum
    column_infos, cell_values = get_type_info(is_enum)
    keys, headers, widths = ([c[i] for c in column_infos] for i in range(3))
    formatter = TableFormatter(all_types=all_types, headers=headers, keys=keys,
                               widths=widths, cell_values=cell_values)
    return formatter


def make_table(all_types, data_type):
    formatter = make_table_formatter(all_types, data_type)
    lines = formatter.make_table(data_type)
    table = "\n".join(lines) + "\n"

    return table


def update_table_files(type_name=None):
    all_types = common.read_types()
    if type_name is None:
        type_names = sorted(all_types.keys())
    else:
        type_names = [type_name]

    for type_name in type_names:
        data_type = common.get_type(all_types, type_name)
        table = make_table(all_types, data_type)
        text = TABLE_COMMENT + table
        rest_path = data_type.table_path
        dir_path = os.path.dirname(rest_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        common.write_file(rest_path, text)


def analyze_types():
    dir_path = os.path.join(common.YAML_DIR, 'elements')
    yaml_paths = common.get_all_files(dir_path, ext='.yaml')
    values = {}
    i = 0
    for yaml_path in yaml_paths:
#        _log.info("processing: {0}".format(path))
        formatter = make_table_formatter(yaml_path)
        type_info = common.read_type(yaml_path)
        type_yaml = common.read_yaml(yaml_path)
        tags_data = type_info['tags']
        tags_yaml = type_yaml['tags']
        for tag, tag_yaml in zip(tags_data, tags_yaml):
            tag_name = tag[TAG_KEY_NAME]
            tag_type = tag[TAG_KEY_TYPE]
            required = common.get_tag_value(tag, TAG_KEY_REQUIRED)
            if 'on_error_custom' in tag and 'error_then' not in tag:
                print(yaml_path, tag_name)
        #common.write_yaml(type_yaml, yaml_path)
    #pprint(values)


class TableFormatter(object):

    # The size of the left and right margin of each cell as a number of spaces.
    margin = 1

    def __init__(self, all_types, cell_values, headers, keys, widths):
        """
        Arguments:
          cell_values:

        """
        self.all_types = all_types
        self.cell_values = cell_values
        self.headers = headers
        self.keys = keys
        self.min_widths = widths

    def wrap(self, text, width):
        return textwrap.wrap(text, width=width, break_long_words=False,
                             break_on_hyphens=False)

    def get_cell_value(self, tag_data, key):
        """
        Return the text to put in the cell of a reST table.
        """
        data_value = common.get_tag_value(self.all_types, tag_data, key)
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

    def make_table(self, data_type):
        """
        Return the reST table for an object type.

        The table is returned as a list of lines of text.
        """
        try:
            tags = data_type.tags
            widths = self.make_widths(self.headers, tags)
            lines = [self.make_divider(widths)]
            lines.extend(self.make_row(self.headers, widths, separator='='))
            for tag in tags:
                lines.extend(self.make_row_from_data(tag, widths=widths))
        except Exception:
            raise Exception("with data_type:\n{0}".format(data_type))
        return lines
