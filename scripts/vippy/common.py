from contextlib import contextmanager
import copy
import logging
import os.path
from pprint import pformat, pprint

import yaml


_log = logging.getLogger()

AUTO_GENERATED_DIR = 'docs/built_rst'
YAML_DIR = 'docs/yaml'
TABLES_DIR = os.path.join(AUTO_GENERATED_DIR, 'tables')
XML_DIR = os.path.join(AUTO_GENERATED_DIR, 'xml')

TAG_KEY_NAME = '_name'
TAG_KEY_TYPE = 'type'
TAG_KEY_REQUIRED = 'required'
TAG_KEY_REPEATING = 'repeating'
TAG_KEY_DESCRIPTION = 'description'
# The error_handling key corresponds to the aggregate error-handling tag
# value and does not correspond to a literal key-value in the YAML data.
TAG_KEY_ERROR_HANDLE = 'error_handling'
TAG_KEY_ERROR_BASE = 'error'
TAG_KEY_ERROR_THEN = 'error_then'
TAG_KEY_ERROR_EXTRA = 'error_extra'

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


def reverse_map(mapping):
    inverted = {}
    for k, v in mapping.items():
        if v in inverted:
            raise Exception("key appears twice: {0}".format(key))
        inverted[v] = k
    return inverted


def read_file(path):
    with open(path, encoding='utf-8') as f:
        text = f.read()
    return text


@contextmanager
def detect_change(path):
    """A context manager for logging whether a text file changes."""
    if os.path.exists(path):
        text = read_file(path)
    else:
        text = None
    yield
    # Check whether the file changed.
    new_text = read_file(path)
    if new_text != text:
        _log.info("updated: {0}".format(path))


def write_file(path, text):
    """Write to a file, and return whether the file changed."""
    with detect_change(path):
        with open(path, mode='w', encoding='utf-8') as f:
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
    """Write a YAML file, and return whether the file changed."""
    with detect_change(path):
        with open(path, "w", encoding='utf-8') as f:
            yaml_dump(data, f)


def normalize_yaml(path):
    """Normalize a YAML file, and return whether the file changed."""
    data = read_yaml(path)
    changed = write_yaml(data, path)
    return changed


def read_type(parent_dir, rel_path):
    yaml_path = os.path.join(parent_dir, rel_path)
    type_yaml = read_yaml(yaml_path)
    data_type = DataType.from_yaml(type_yaml, rel_path=rel_path)
    return data_type


class AllTypes:

    def __init__(self, type_map):
        """
        Arguments:
          type_map: map from type name to DataType object.  Examples of type
            names include "BallotMeasureContest" in the case of elements and
            "DistrictType" in the case of enumerations.
        """
        self.elements = []
        self.enumerations = []
        self.sub_types = set()
        self.type_map = type_map


def get_all_types():
    """
    Read all YAML files, and return an AllTypes object.
    """
    parent_dir = YAML_DIR
    types_map = {}
    all_types = AllTypes(types_map)
    rel_paths = get_all_files(parent_dir, ext='.yaml')
    for rel_path in rel_paths:
        data_type = read_type(parent_dir, rel_path)
        type_name = data_type.name
        types_map[type_name] = data_type
        if data_type.is_enum:
            seq = all_types.enumerations
        else:
            seq = all_types.elements
        seq.append(data_type)

    for data_type in types_map.values():
        sub_types = data_type.sub_types
        for sub_type in sub_types:
            data_type = types_map[sub_type]
            data_type.is_sub_type = True

    return all_types


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
        value = tag_data[key]
    except KeyError:
        value = DEFAULT_TAG_VALUES[key]
    return value


def make_error_if(all_types, tag_data):
    noun = 'field' if is_tag_field(all_types, tag_data) else 'element'
    required = get_simple_tag_value(tag_data, TAG_KEY_REQUIRED)
    condition = 'invalid' if required else 'invalid or not present'

    return "the {noun} is {condition},".format(noun=noun, condition=condition)


def make_error_if_then(all_types, tag_data, error_then):
    if error_then.startswith('='):
        error_then_format = _ERROR_THENS[error_then]
        containing_type = tag_data['containing_type']
        error_then = error_then_format.format(containing_type=containing_type)
    error_if = make_error_if(all_types, tag_data)
    error = "If {0} then {1}".format(error_if, error_then)

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


def make_error_base(all_types, tag_data):
    try:
        error = tag_data[TAG_KEY_ERROR_BASE]
    except KeyError:
        error = make_error_default(all_types, tag_data)
    return error


def make_error_initial(all_types, tag_data):
    try:
        error_then = tag_data[TAG_KEY_ERROR_THEN]
    except KeyError:
        error = make_error_base(all_types, tag_data)
    else:
        error = make_error_if_then(all_types, tag_data, error_then)

    return error


def get_error_handling_value(all_types, tag_data):
    """
    Here is a description in human terms of how this value is calculated:

    1. If the "error_then" YAML value is present, then construct the
       standard "If ... then ..." phrase using our template.
    2. If "error_then" is not present, then use the "error" value.
    3. TODO (finish this description)
    4. Lastly, if the "error_extra" YAML value is present, then add it
       to the end of the string we have built so far from the previous
       steps.

    """
    error = make_error_initial(all_types, tag_data)
    try:
        error_extra = tag_data[TAG_KEY_ERROR_EXTRA]
    except KeyError:
        pass
    else:
        error += " " + error_extra

    return error


def get_tag_value(all_types, tag_data, key):
    """
    Return the "pre-conversion" value to put in a cell of a reST table.
    """
    try:
        if key == TAG_KEY_ERROR_HANDLE:
            # We use extra logic to derive the error-handling value.
            value = get_error_handling_value(all_types, tag_data)
        else:
            value = get_simple_tag_value(tag_data, key)
    except Exception:
        raise Exception("tag_data: {0}".format(pformat(tag_data)))

    return value


class DataType(object):

    @classmethod
    def from_yaml(cls, type_yaml, rel_path):
        """
        Create a DataType object from the information in a YAML file.

        Arguments:
          type_yaml: the contents of a YAML file deserialized as a
            Python object.
          rel_path: the path to the YAML file relative to the TODO
            directory.
        """
        file_name = os.path.basename(rel_path)
        snake_name, ext = os.path.splitext(file_name)

        type_name = type_yaml['_name']
        type_data = copy.deepcopy(type_yaml)
        tags = type_data.get('tags', [])
        for tag in tags:
            tag['containing_type'] = type_name

        is_enum = 'enumerations' in rel_path

        return cls(type_yaml, type_data, rel_path, snake_name=snake_name, is_enum=is_enum)

    def __init__(self, yaml, data, rel_path, snake_name, is_enum):
        self.data = data
        self.is_enum = is_enum
        self.is_sub_type = False
        self.rel_path = rel_path
        self.snake_name = snake_name
        self.yaml = yaml

    def __repr__(self):
        return ("<DataType object (name={0!r}, rel_path={1!r})>"
                .format(self.name, self.rel_path))

    @property
    def name(self):
        return self.data['_name']

    @property
    def spinal_name(self):
        return self.snake_name.replace("_", "-")

    @property
    def sub_types(self):
        return self.data.get('_sub_types', [])

    @property
    def tags(self):
        return self.data.get('tags')

    @property
    def table_path(self):
        """Return a path relative to the repo root."""
        if not self.tags:
            return
        return self.get_rest_path(TABLES_DIR)

    @property
    def rest_path(self):
        """Return a path relative to the repo root."""
        return self.get_rest_path(XML_DIR)

    def get_rest_path(self, dir_path):
        rel_path = self.rel_path
        root, ext = os.path.splitext(rel_path)
        rest_rel_path = "{0}.rst".format(root)
        path = os.path.join(dir_path, rest_rel_path)
        return path
