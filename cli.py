import argparse
import re
import sys
import functools as ft

from typing import (
    Any,
    Callable,
    Optional,
)


def compile_cli() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='')

    parser.add_argument('-p',
                        '--project-path',
                        default='.',
                        help='Path to the project.')

    parser.add_argument('-v',
                        '--view-exclusions',
                        action='store_true',
                        help='Prints exclusions to stdout.')

    parser.add_argument('-m',
                        '--modify-exclusion',
                        action='append',
                        help='Modify an exisiting exclusion, must be in the '
                             'format "number:new_exclusion_string" (without '
                             'quotation marks). Multiple modifications must '
                             'flagged individually, e.g. '
                             '"python -m dirtree -m 0:hello -m 1:hi"')

    parser.add_argument('-s',
                        '--subtract-exclusion',
                        type=int,
                        action='append',
                        help='Remove an existing exclusion, pass the exclusion '
                             'number. Multiple subtractions must be flagged '
                             'individually, e.g. '
                             '"python -m dirtree -s 1 -s 2"')

    parser.add_argument('-a',
                        '--add-exclusions',
                        nargs='+',
                        help='Append to the exclusion list. Can list multiple '
                             'exclusions at once, e.g. '
                             '"python -m dirtree -a hello hi there"')

    parser.add_argument('-d',
                        '--delete-all-exclusions',
                        action='store_true',
                        help='Deletes all exclusions.')

    return parser


def cli(argvs: Optional[list[str]] = None):
    argvs = argvs or sys.argv[1:]
    parser = compile_cli()
    return parser.parse_args(argvs)

