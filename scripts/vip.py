"""
Entry point for the reST script for VIP contributors.

reStructuredText (aka reST) [1] is a markup language used for
documentation.  VIP uses reST for its documentation.

This script is mainly for auto-generating much of the reST markup
(especially the reST that involve tables).


[1] reST: http://docutils.sourceforge.net/rst.html

"""

import argparse
import logging
import os
import sys
import textwrap
from vippy import common
from vippy.common import XML_DIR
from vippy import rest


_log = logging.getLogger()

FORMATTER_CLASS = argparse.RawDescriptionHelpFormatter

HELP_SUMMARY = """\
Helper script for VIP contributors.
"""


def _wrap(text):
    """Format text for help output."""
    paras = text.split("\n\n")
    paras = [textwrap.fill(p) for p in paras]
    text = "\n\n".join(paras)

    return text


def ns_to_paths(ns, parent_dir, ext):
    """Return the list of paths specified by an argparse.Namespace object."""
    path = ns.path
    if path:
        paths = [path]
    else:
        rel_paths = common.get_all_files(parent_dir, ext=ext)
        paths = [os.path.join(parent_dir, p) for p in rel_paths]
    return paths


def command_norm_yaml(ns):
    """Run the norm_yaml command."""
    parent_dir = common.YAML_DIR
    paths = ns_to_paths(ns, parent_dir=parent_dir, ext=".yaml")
    for path in paths:
        common.normalize_yaml(path)


def command_make_rest(ns):
    """Run the make_rest command."""
    rest.update_rest_files(ns.type_name)


def command_scratch(ns):
    """Run the scratch command."""
    rest.analyze_types()


def make_subparser(sub, command_name, help, command_func=None, details=None, **kwargs):
    """
    Create the "sub-parser" for our command-line parser.

    This facilitates having multiple "commands" for a single script,
    for example "norm_yaml", "make_rest", etc.
    """
    if command_func is None:
        command_func_name = "command_{0}".format(command_name)
        command_func = globals()[command_func_name]

    # Capitalize the first letter for the long description.
    desc = help[0].upper() + help[1:]
    if details is not None:
        desc += "\n\n{0}".format(details)
    desc = _wrap(desc)
    parser = sub.add_parser(
        command_name,
        formatter_class=FORMATTER_CLASS,
        help=help,
        description=desc,
        **kwargs
    )
    parser.set_defaults(run_command=command_func)
    return parser


def create_parser():
    """
    Create the command-line parser.

    Returns an ArgumentParser object.
    """
    root_parser = argparse.ArgumentParser(
        formatter_class=FORMATTER_CLASS, description=HELP_SUMMARY
    )
    sub = root_parser.add_subparsers(help="sub-command help")

    parser = make_subparser(
        sub,
        "norm_yaml",
        help=(
            "normalize one or more YAML files.  This command does things "
            "like alphabetize the keys in the YAML files, normalize the "
            "spacing, etc."
        ),
    )
    parser.add_argument(
        "path",
        metavar="PATH",
        nargs="?",
        help="a path to a YAML file. Defaults to all files.",
    )

    parser = make_subparser(
        sub, "make_rest", help=("update all reST files from the YAML files.")
    )
    parser.add_argument(
        "type_name",
        metavar="TYPE_NAME",
        nargs="?",
        help=('the name of a type (e.g. "HoursOpen"). ' "Defaults to all types."),
    )

    parser = make_subparser(
        sub,
        "scratch",
        help=(
            "temporary command for development purposes. You can "
            "use / modify this command if you ever need a command for "
            "experimental purposes (e.g. to analyze the contents of "
            "the YAML files)."
        ),
    )

    return root_parser


def main(argv=None):
    """
    Starting point for the script.

    This is what gets executed when the following is run from the
    repository root:

      $ python <path-to-this-file>

    """
    if argv is None:
        argv = sys.argv[1:]
    logging.basicConfig(
        level="DEBUG", style="{", format="vippy: [{levelname}] {message}"
    )
    common.configure_yaml()
    parser = create_parser()
    ns = parser.parse_args(argv)  # an argparse.Namespace object.
    try:
        ns.run_command
    except AttributeError:
        # We need to handle this exception because of the following
        # behavior change:
        #   http://bugs.python.org/issue16308
        parser.print_help()
    else:
        ns.run_command(ns)


if __name__ == "__main__":
    main()
