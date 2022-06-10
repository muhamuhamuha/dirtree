import pytest
from pathlib import Path
# from pytest_lazy_fixture import lazy_fixture

from tree import tree, EXCEPT

@pytest.mark.parametrize(
    'path, excepts', [
        # (Path.cwd(), '__pycache__'),
        # (Path.cwd(), '__pycache__|\.pytest_cache|.vscode'),
        (Path.cwd().parent / 'hl7lib', EXCEPT)
    ]
)
def test_tree(path, excepts):
    for line in tree(path, excepts):
        print(line)

