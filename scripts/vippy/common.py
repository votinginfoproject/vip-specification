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

import copy
import logging
import os.path
from pprint import pformat

import yaml


_log = logging.getLogger()

DATA_DIR = 'docs/data'
TABLES_DIR = 'docs/tables'
XML_DIR = 'docs/xml'

TAG_KEY_NAME = '_name'
TAG_KEY_TYPE = 'type'
TAG_KEY_REQUIRED = 'required'
TAG_KEY_REPEATING = 'repeating'
TAG_KEY_DESCRIPTION = 'description'
TAG_KEY_ERROR_HANDLE = 'error_handling'

_TAG_KEY_ERROR = 'error'
_TAG_KEY_ERROR_THEN = 'error_then'
_TAG_KEY_ERROR_EXTRA = 'error_extra'

DEFAULT_TAG_VALUES = {
    TAG_KEY_REQUIRED: False,
    TAG_KEY_REPEATING: False,
}

_ERROR_FORMAT_STRING = ("the implementation {action} ignore {ignore}.")

_ERROR_THEN_FORMAT_REQUIRED = _ERROR_FORMAT_STRING.format(action='is required to',
                                    ignore='the ``{containing_type}`` element containing it')

_ERROR_THENS = {
    '=must-ignore': _ERROR_FORMAT_STRING.format(action='is required to', ignore='it'),
    '=should-ignore': _ERROR_FORMAT_STRING.format(action='should', ignore='it'),
}

TYPE_MAP = {
    ':doc:`BallotMeasureType <../enumerations/ballot_measure_type>`': 'BallotMeasureType',
    ':doc:`CandidatePostElectionStatus <../enumerations/candidate_post_election_status>`': 'CandidatePostElectionStatus',
    ':doc:`CandidatePreElectionStatus <../enumerations/candidate_pre_election_status>`': 'CandidatePreElectionStatus',
    ':doc:`ContactInformation <contact_information>`': 'ContactInformation',
    ':ref:`Department <ea-dep>`': 'Department',
    ':doc:`DistrictType <../enumerations/district_type>`': 'DistrictType',
    '`ExternalIdentifier`_': 'ExternalIdentifier',
    ':doc:`ExternalIdentifiers <external_identifiers>`': 'ExternalIdentifiers',
    '`Hours`_': 'Hours',
    '`HtmlColorString`_': 'HtmlColorString',
    ':doc:`IdentifierType <../enumerations/identifier_type>`': 'IdentifierType',
    ':doc:`InternationalizedText <internationalized_text>`': 'InternationalizedText',
    '`Schedule`_': 'Schedule',
    '`LanguageString`_': 'LanguageString',
    '`LatLng`_': 'LatLng',
    '`NonHouseAddress`_': 'NonHouseAddress',
    ':doc:`OebEnum <../enumerations/oeb_enum>`': 'OebEnum',
    ':doc:`OfficeTermType <../enumerations/office_term_type>`': 'OfficeTermType',
    '`Schedule`_': 'Schedule',
    '`Term`_': 'Term',
    '`TimeWithZone`_': 'TimeWithZone',
    ':doc:`VoteVariation <../enumerations/vote_variation>`': 'VoteVariation',
    ':ref:`VoterService <ea-dep-voter-service>`': 'VoterService',
    ':doc:`VoterServiceType <../enumerations/voter_service_type>`': 'VoterServiceType',
}

ERROR_MAP = {
    'If the element is invalid or not present, the implementation is required to ignore it.': '=must-ignore',
    'If the element is invalid or not present, then the implementation is required to ignore it.': '=must-ignore',
    'If the element is invalid or not present, the implementation should ignore it.': '=should-ignore',
    'If the field is invalid or not present, the implementation is required to ignore it.': '=must-ignore',
    'If the field is invalid or not present, the implementation should ignore it.': '=should-ignore',
    'If the field is invalid or not present, then the implementation is required to ignore it.': '=must-ignore',
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


def reverse_map(mapping):
    inverted = {}
    for k, v in mapping.items():
        if v in inverted:
            raise Exception("key appears twice: {0}".format(key))
        inverted[v] = k
    return inverted


def write(path, text):
    _log.info("writing to: {0}".format(path))
    with open(path, mode='w') as f:
        f.write(text)


def get_all_files(parent_dir, ext=None):
    """Return a list of paths relative to the given dir_path."""
    paths = []
    for root_dir, dir_paths, file_names in os.walk(parent_dir):
        for file_name in file_names:
            path = os.path.join(root_dir, file_name)
            rel_path = os.path.relpath(path, start=parent_dir)
            paths.append(rel_path)
    if ext is not None:
        paths = [p for p in paths if os.path.splitext(p)[1] == ext]

    return paths


# The idea for this comes from here:
# http://stackoverflow.com/questions/8640959/how-can-i-control-what-scalar-form-pyyaml-uses-for-my-data
def _yaml_str_representer(dumper, data):
    """A PyYAML representer that uses literal blocks for multi-line strings.

    For example--

      long: |
        This is
        a multi-line
        string.
      short: This is a one-line string.
    """
    style = '|' if '\n' in data else None
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style=style)


def configure_yaml():
    yaml.add_representer(str, _yaml_str_representer)


def read_yaml(path):
    with open(path) as f:
        data = yaml.load(f)
    return data


def yaml_dump(*args):
    return yaml.dump(*args, default_flow_style=False, allow_unicode=True,
                     default_style=None)


def write_yaml(data, path):
    with open(path, "w") as f:
        yaml_dump(data, f)


def normalize_yaml(path):
    data = read_yaml(path)
    write_yaml(data, path)


def read_type(parent_dir, rel_path):
    yaml_path = os.path.join(parent_dir, rel_path)
    type_yaml = read_yaml(yaml_path)
    data_type = DataType.from_yaml(type_yaml, rel_path=rel_path)
    return data_type


def read_types():
    parent_dir = DATA_DIR
    data_types = {}
    rel_paths = get_all_files(parent_dir, ext='.yaml')
    for rel_path in rel_paths:
        data_type = read_type(parent_dir, rel_path)
        type_name = data_type.name
        data_types[type_name] = data_type

    return data_types


def get_type(all_types, type_name):
    try:
        data_type = all_types[type_name]
    except KeyError:
        all_names = sorted(all_types.keys())
        raise Exception("available type names: {0}".format(", ".join(all_names)))

    return data_type


def is_tag_field(all_types, tag_data):
    type_name = tag_data[TAG_KEY_TYPE]
    try:
        data_type = all_types[type_name]
    except KeyError:
        # Then we assume it is a simple type like "xs:string" or "TimeWithZone".
        return True
    return data_type.is_enum


def get_simple_tag_value(tag_data, key):
    """This works for everything except for the error values."""
    try:
        try:
            value = tag_data[key]
        except KeyError:
            value = DEFAULT_TAG_VALUES[key]
    except Exception:
        raise Exception("tag_data: {0}".format(pformat(tag_data)))

    return value


def make_error_if(all_types, tag_data):
    noun = 'field' if is_tag_field(all_types, tag_data) else 'element'
    required = get_simple_tag_value(tag_data, TAG_KEY_REQUIRED)
    condition = 'invalid' if required else 'invalid or not present'

    return "If the {noun} is {condition},".format(noun=noun, condition=condition)


def make_error_if_then(all_types, tag_data, error_then):
    if error_then.startswith('='):
        error_then_format = _ERROR_THENS[error_then]
        containing_type = tag_data['containing_type']
        error_then = error_then_format.format(containing_type=containing_type)
    error_if = make_error_if(all_types, tag_data)
    error = "{0} then {1}".format(error_if, error_then)

    return error


def make_error_default(all_types, tag_data):
    required = get_simple_tag_value(tag_data, TAG_KEY_REQUIRED)
    if not required:
        raise Exception('we have not defined a default "error" value for '
                        "tags that are not required.\n"
                        "tag data:\n{0}".format(pformat(tag_data)))
    error_then = _ERROR_THEN_FORMAT_REQUIRED.format(**tag_data)
    error = make_error_if_then(all_types, tag_data, error_then)
    return error


def make_error(all_types, tag_data):
    try:
        error = tag_data[_TAG_KEY_ERROR]
    except KeyError:
        error = make_error_default(all_types, tag_data)
    return error


def make_error_initial(all_types, tag_data):
    try:
        error_then = tag_data[_TAG_KEY_ERROR_THEN]
    except KeyError:
        error = make_error(all_types, tag_data)
    else:
        error = make_error_if_then(all_types, tag_data, error_then)

    return error


def get_error_value(all_types, tag_data):
    error = make_error_initial(all_types, tag_data)
    try:
        error_extra = tag_data[_TAG_KEY_ERROR_EXTRA]
    except KeyError:
        pass
    else:
        error += " " + error_extra

    return error


def get_tag_value(all_types, tag_data, key):
    if key == TAG_KEY_ERROR_HANDLE:
        value = get_error_value(all_types, tag_data)
    else:
        value = get_simple_tag_value(tag_data, key)

    return value


class DataType(object):

    @classmethod
    def from_yaml(cls, type_yaml, rel_path):
        file_name = os.path.basename(rel_path)
        snake_name, ext = os.path.splitext(file_name)

        type_name = type_yaml['name']
        type_data = copy.deepcopy(type_yaml)
        tags = type_data['tags']
        for tag in tags:
            tag['containing_type'] = type_name

        is_enum = 'enumerations' in rel_path

        return cls(type_yaml, type_data, rel_path, snake_name=snake_name, is_enum=is_enum)

    def __init__(self, yaml, data, rel_path, snake_name, is_enum):
        self.data = data
        self.is_enum = is_enum
        self.rel_path = rel_path
        self.snake_name = snake_name
        self.yaml = yaml

    def __repr__(self):
        return ("<DataType object (name={0!r}, path={1!r})>"
                .format(self.name, self.rel_path))

    @property
    def name(self):
        return self.data['name']

    @property
    def tags(self):
        return self.data['tags']

    @property
    def table_path(self):
        """Return a path relative to the repo root."""
        rel_path = self.rel_path
        root, ext = os.path.splitext(rel_path)
        rest_rel_path = "{0}.rst".format(root)
        path = os.path.join(TABLES_DIR, rest_rel_path)
        return path
