import re
import pytest
from collections import defaultdict
from pathlib import Path

from dirty import *


@pytest.mark.parametrize(
    'path, exclude, expected_tees, expected_lasts', [
        (
            Path.cwd(),
            EXCLUDE,
            [
                '.gitignore',
                'README.md',
                'requirements-dev.txt',
                'test_tree.py'
            ],
            ['tree.py']
        ),
        (
            Path.cwd(),
            EXCLUDE.replace('|\\.vscode', ''),
            [
                '.gitignore',
                '.vscode',
                'launch.json',
                'README.md',
                'requirements-dev.txt',
                'test_tree.py'
            ],
            ['settings.json', 'tree.py']
        ),
    ]
)
def test_tree_prints_out_all_contents(path: Path,
                                      exclude: RegEx,
                                      expected_tees: list[str],
                                      expected_lasts: list[str],
                                      capsys: pytest.CaptureFixture):

    for line in tree(path, exclude):
        print(line)

    out, _ = capsys.readouterr()

    # partition will split into a 3 item tuple TEE or LAST
    # the first item will be '' or BRANCHs and SPACEs
    # the second item will be TEE or LAST
    # the third will be the directory or file
    categorized = [t.partition(TEE)
                   if TEE in t else
                   t.partition(LAST)
                   for t in out.strip().split('\n')]

    grouper = defaultdict(list)
    for nests, branches, path_name in categorized:
        grouper[branches].append(path_name)

    assert grouper[TEE] == expected_tees
    assert grouper[LAST] == expected_lasts

