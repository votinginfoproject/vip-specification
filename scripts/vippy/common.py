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

import logging
import os.path

import yaml


_log = logging.getLogger()

DATA_DIR = 'docs/data'
TABLES_DIR = 'docs/tables'
XML_DIR = 'docs/xml'

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


def write(path, text):
    _log.info("writing to: {0}".format(path))
    with open(path, mode='w') as f:
        f.write(text)


def get_all_files(dir_path, ext=None):
    paths = []
    for root_dir, dir_paths, file_names in os.walk(dir_path):
        for file_name in file_names:
            path = os.path.join(root_dir, file_name)
            paths.append(path)
    if ext is not None:
        paths = [p for p in paths if os.path.splitext(p)[1] == ext]

    return paths


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

REQUIRED_MAP = {
    'Optional': None,
    '**Required**': True,
}

def analyze_types():
    dir_path = os.path.join(DATA_DIR, 'elements')
    yaml_paths = get_all_files(dir_path, ext='.yaml')
    key = 'required'
    for path in yaml_paths:
        data = read_yaml(path)
        tags_data = data['tags']
        for tag_data in tags_data:
            value = tag_data[key]
            value = REQUIRED_MAP.get(value, value)
            if not value:
                del tag_data[key]
            else:
                tag_data[key] = value
        write_yaml(data, path)
