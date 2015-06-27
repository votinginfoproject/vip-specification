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

"""Entry point for main developer script.

Usage:

  $ python scripts/vip.py -h

"""

import argparse
import logging
import os
import subprocess
import sys
import textwrap

from vippy import common
from vippy import rest


_log = logging.getLogger()

DATA_DIR = 'docs/data'
FORMATTER_CLASS = argparse.RawDescriptionHelpFormatter

DESCRIPTION = """\
Helper script for contributors to the vip-specification repo.
"""

def _wrap(text):
    """Format text for help outuput."""
    paras = text.split("\n\n")
    paras = [textwrap.fill(p) for p in paras]
    text = "\n\n".join(paras)

    return text


def _get_all_files(dir_path):
    paths = []
    for root_dir, dir_paths, file_names in os.walk(dir_path):
        for file_name in file_names:
            path = os.path.join(root_dir, file_name)
            paths.append(path)

    return paths


def command_make_table(ns):
    path = ns.path
    if path:
        paths = [path]
    else:
        paths = _get_all_files(DATA_DIR)
        paths = [p for p in paths if os.path.splitext(p)[1] == '.yaml']
    for path in paths:
        rest.make_table(path)


def command_norm_yaml(ns):
    path = ns.path
    if path:
        paths = [path]
    else:
        paths = _get_all_files(DATA_DIR)
        paths = [p for p in paths if os.path.splitext(p)[1] == '.yaml']
    for path in paths:
        common.normalize_yaml(path)


def make_subparser(sub, command_name, help, command_func=None, details=None, **kwargs):
    if command_func is None:
        command_func_name = "command_{0}".format(command_name)
        command_func = globals()[command_func_name]

    # Capitalize the first letter for the long description.
    desc = help[0].upper() + help[1:]
    if details is not None:
        desc += "\n\n{0}".format(details)
    desc = _wrap(desc)
    parser = sub.add_parser(command_name, formatter_class=FORMATTER_CLASS,
                            help=help, description=desc, **kwargs)
    parser.set_defaults(run_command=command_func)
    return parser


def create_parser():
    """Return an ArgumentParser object."""
    root_parser = argparse.ArgumentParser(formatter_class=FORMATTER_CLASS,
            description=DESCRIPTION)
    sub = root_parser.add_subparsers(help='sub-command help')

    parser = make_subparser(sub, "norm_yaml",
                help="normalize one or more YAML files.")
    parser.add_argument('--all', dest='all', action='store_true',
        help='normalize all YAML files.')
    parser.add_argument('path', metavar='PATH', nargs='?',
        help="a path to a YAML file.")

    parser = make_subparser(sub, "make_table",
                help="make a reST table.")
    parser.add_argument('--all', dest='all', action='store_true',
        help='make all reST tables.')
    parser.add_argument('path', metavar='PATH', nargs='?',
        help="a path to a YAML file.")

    return root_parser


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    logging.basicConfig(level='INFO')
    common.configure_yaml()
    parser = create_parser()
    ns = parser.parse_args(argv)
    try:
        ns.run_command
    except AttributeError:
        # We need to handle this exception because of the following
        # behavior change:
        #   http://bugs.python.org/issue16308
        parser.print_help()
    else:
        ns.run_command(ns)


if __name__ == '__main__':
    main()
