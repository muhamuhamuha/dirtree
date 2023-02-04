import pytest

import re
from collections import defaultdict
from pathlib import Path

import dirtree



@pytest.mark.parametrize(
    'exclusions, mods, expected', [
        (
            {0: 'hi', 1: 'bye'},
            ['0:hello'],
            {0: 'hello', 1: 'bye'}
        ),
        (
            {0: 'hi', 1: 'bye'},
            ['0:hello', '1:2'],
            {0: 'hello', 1: '2'}
        ),
        (
            {0: 'hi'},
            [],
            {0: 'hi'},
        ),
    ]
)
def test_modify_exclusions(exclusions: dict,
                           mods: list[str],
                           expected: dict):
    new_exclusions = dirtree.modify_exclusions(exclusions, mods)
    assert new_exclusions == expected


@pytest.mark.parametrize(
    'exclusions, adds, expected', [
        (
            {0: 'hi', 1: 'bye'},
            ['hello'],
            {0: 'hi', 1: 'bye', 2: 'hello'},
        ),
        (
            {0: 'hi', 2: 'hello'},
            ['goodbye'],
            {0: 'hi', 2: 'hello', 3: 'goodbye'},
        ),
    ]
)
def test_add_exclusions(exclusions: dict,
                        adds: list[str],
                        expected: dict):
    new_exclusions = dirtree.add_exclusions(exclusions, adds)
    assert new_exclusions == expected

#@pytest.mark.parametrize(
#    'path, exclude, expected_tees, expected_lasts', [
#        (
#            Path.cwd().parents[1] / 'sql' / 'jaffle_shop',
#            dirtree.EXCLUSIONS + '|etc|seeds',
#            [
#                '.gitignore',
#                'README.md',
#                'requirements-dev.txt',
#                'test_tree.py'
#            ],
#            ['tree.py']
#        ),
#        (
#            Path.cwd(),
#            dirtree.EXCLUSIONS,
#            [
#                '.gitignore',
#                'README.md',
#                'requirements-dev.txt',
#                'test_tree.py'
#            ],
#            ['tree.py']
#        ),
#        (
#            Path.cwd(),
#            dirtree.EXCLUSIONS.replace('|\\.vscode', ''),
#            [
#                '.gitignore',
#                '.vscode',
#                'launch.json',
#                'README.md',
#                'requirements-dev.txt',
#                'test_tree.py'
#            ],
#            ['settings.json', 'tree.py']
#        ),
#    ]
#)
#def test_tree_prints_out_all_contents(path: Path,
#                                      exclude: RegEx,
#                                      expected_tees: list[str],
#                                      expected_lasts: list[str],
#                                      capsys: pytest.CaptureFixture):
#    for line in dirtree.dirtree(path, exclude):
#        print(line)
#
#    out, _ = capsys.readouterr()
#    breakpoint()
#
#    # partition will split into a 3 item tuple TEE or LAST
#    # the first item will be '' or BRANCHs and SPACEs
#    # the second item will be TEE or LAST
#    # the third will be the directory or file
#    categorized = [t.partition(TEE)
#                   if TEE in t else
#                   t.partition(LAST)
#                   for t in out.strip().split('\n')]
#
#    grouper = defaultdict(list)
#    for nests, branches, path_name in categorized:
#        grouper[branches].append(path_name)
#
#    assert grouper[TEE] == expected_tees
#    assert grouper[LAST] == expected_lasts

