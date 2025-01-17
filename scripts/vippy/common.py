from contextlib import contextmanager
from pprint import pformat
import copy
import logging
import os.path
import yaml

_log = logging.getLogger()

AUTO_GENERATED_DIR = "docs/built_rst"
YAML_DIR = "docs/yaml"
XML_DIR = os.path.join(AUTO_GENERATED_DIR, "xml")
CSV_DIR = os.path.join(AUTO_GENERATED_DIR, "csv")
TAG_KEY_REQUIRED = "required"
TAG_KEY_TYPE = "type"
TAG_KEY_ERROR_HANDLING = "error_handling"
TAG_KEY_NAME = "_name"
TAG_KEY_REPEATING = "repeating"
TAG_KEY_DESCRIPTION = "description"
TAG_KEY_EXTENDS = "extends"
TAG_KEY_CSV_TYPE = "csv-type"
TAG_KEY_CSV_HEADER_NAME = "csv-header-name"


def reverse_map(mapping):
    inverted = {}
    for k, v in mapping.items():
        if v in inverted:
            raise Exception("key appears twice: {0}".format(key))
        inverted[v] = k
    return inverted


def read_file(path):
    with open(path, encoding="utf-8") as f:
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
        with open(path, mode="w", encoding="utf-8") as f:
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
    style = "|" if "\n" in data else None
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style=style)


def configure_yaml():
    yaml.add_representer(str, _yaml_str_representer)


def read_yaml(path):
    # https://github.com/yaml/pyyaml/wiki/PyYAML-yaml.load(input)-Deprecation
    with open(path) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data


def yaml_dump(*args):
    return yaml.dump(
        *args, default_flow_style=False, allow_unicode=True, default_style=None
    )


def write_yaml(data, path):
    """Write a YAML file, and return whether the file changed."""
    with detect_change(path):
        with open(path, "w", encoding="utf-8") as f:
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
        self.extends = set()
        self.type_map = type_map


def get_all_types():
    """
    Read all YAML files, and return an AllTypes object.
    """
    parent_dir = YAML_DIR
    types_map = {}
    all_types = AllTypes(types_map)
    rel_paths = get_all_files(parent_dir, ext=".yaml")
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
        extends = data_type.extends
        for sub_type in sub_types:
            sub_data_type = types_map[sub_type]
            sub_data_type.is_sub_type = True
        for extend in extends:
            extended_data_type = types_map[extend]
            extended_data_type.is_extends = True

    return all_types


def get_type(all_types, type_name):
    try:
        data_type = all_types[type_name]
    except KeyError:
        all_names = sorted(all_types.keys())
        raise Exception("available type names: {0}".format(", ".join(all_names)))

    return data_type


def get_simple_tag_value(tag_data, key):
    """This works for everything except for the error values."""
    if key not in tag_data and key in ["required", "repeating"]:
        return False
    elif key in tag_data:
        return tag_data[key]
    else:
        raise KeyError(key + " not found in tag_data.")


def get_tag_value(all_types, tag_data, key):
    """
    Return the "pre-conversion" value to put in a cell of a reST table.
    """
    if key == "error_handling":
        if "error" in tag_data:
            value = tag_data["error"]
        else:
            value = ""
    else:
        value = get_simple_tag_value(tag_data, key)

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

        type_name = type_yaml["_name"]
        type_data = copy.deepcopy(type_yaml)
        tags = type_data.get("tags", [])
        for tag in tags:
            tag["containing_type"] = type_name

        is_enum = "enumerations" in rel_path

        return cls(
            type_yaml, type_data, rel_path, snake_name=snake_name, is_enum=is_enum
        )

    def __init__(self, yaml, data, rel_path, snake_name, is_enum):
        self.data = data
        self.is_enum = is_enum
        self.is_sub_type = False
        self.is_extends = False
        self.rel_path = rel_path
        self.snake_name = snake_name
        self.yaml = yaml

    def __repr__(self):
        return "<DataType object (name={0!r}, rel_path={1!r})>".format(
            self.name, self.rel_path
        )

    @property
    def name(self):
        return self.data["_name"]

    @property
    def csv_name(self):
        return self.data["csv-header-name"]

    @property
    def csv_type(self):
        return self.data["csv-type"]

    @property
    def skip_element_on(self):
        return self.data.get("skip_element_on", "")

    @property
    def primary_type_on(self):
        return self.data.get("primary_type_on", "")

    @property
    def spinal_name(self):
        return self.snake_name.replace("_", "-")

    @property
    def sub_types(self):
        return self.data.get("_sub_types", [])

    @property
    def extends(self):
        return self.data.get("extends", [])

    @property
    def tags(self):
        return self.data.get("tags")

    @property
    def table_path(self):
        """Return a path relative to the repo root."""
        if not self.tags:
            return
        return self.get_rest_path(TABLES_DIR)

    @property
    def rest_path_csv(self):
        """Return a path relative to the repo root."""
        return self.get_rest_path(CSV_DIR)

    @property
    def rest_path_xml(self):
        """Return a path relative to the repo root."""
        return self.get_rest_path(XML_DIR)

    def get_rest_path(self, dir_path):
        rel_path = self.rel_path
        root, ext = os.path.splitext(rel_path)
        rest_rel_path = "{0}.rst".format(root)
        path = os.path.join(dir_path, rest_rel_path)
        return path

    def make_ref_link(self, prefix):
        """
        Return, for example: ":ref:`single-xml-internationalized-text`".
        """
        return ":ref:`{0}-{1}`".format(prefix, self.spinal_name)
