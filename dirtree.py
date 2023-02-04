import re
from pathlib import Path

from typing import (
    Iterator,
    NewType,
    Optional,
)

RegEx = NewType('RegEx', str)


# prefix components:
SPACE =  '    '
BRANCH = '│   '
# pointers:
TEE =    '├── '
LAST =   '└── '

# exclude directories
EXCLUSIONS: dict[int, str] = dict(
    enumerate([
        r'__pycache__',
        r'\.pytest_cache',
        r'.?venv',
        r'\.vscode',
        r'^\.git$',
        r'\.ipynb_checkpoints',
        r'\.idea',
    ])
)


def modify_exclusions(exclusions: dict[int, str],
                      mods: Optional[list[str]] = None) -> dict[int, str]:
    mods = mods or []
    for mod in mods:
        x, y = mod.split(':')
        exclusions |= {int(x): y}

    return exclusions


def add_exclusions(exclusions: dict[int, str],
                   adds: Optional[list[str]] = None) -> dict[int, str]:
    adds = adds or []
    for a in adds:
        exclusions[max(exclusions.keys()) + 1] = a
    return exclusions


def dirtree(dir_path: Path, exclude: RegEx, prefix: str = '') -> Iterator:
    """
    A recursive generator, given a directory Path object it
    will yield a visual tree structure line by line. Each line is prefixed
    by characters to create a directory tree.
    """
    contents = [p for p in dir_path.iterdir() if not re.match(exclude, p.name)]

    # contents each get pointers that are ├── with a final └── :
    pointers = [TEE] * (len(contents) - 1) + [LAST]

    for pointer, path in zip(pointers, contents):
        yield prefix + pointer + path.name

        # extend the prefix and recurse:
        if path.is_dir() and not re.match(exclude, path.name):
            extension = BRANCH if pointer == TEE else SPACE
            # i.e. SPACE because LAST, └── , above so no more |
            yield from dirtree(path, exclude, prefix=prefix + extension)

