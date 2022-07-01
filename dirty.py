import re
from argparse import ArgumentParser
from pathlib import Path

from typing import Iterator, NewType

RegEx = NewType('RegEx', str)


# prefix components:
SPACE =  '    '
BRANCH = '│   '
# pointers:
TEE =    '├── '
LAST =   '└── '

# exclude directories
EXCLUDE = (
    '__pycache__'
    '|\.pytest_cache'
    '|.?venv'
    '|\.vscode'
    '|^\.git$'
    '|\.ipynb_checkpoints'
    '|\.idea'
)


def dirty(dir_path: Path,
          exclude: RegEx = EXCLUDE,
          prefix: str = '') -> Iterator:
    """
    A recursive generator, given a directory Path object
    will yield a visual tree structure line by line
    with each line prefixed by the same characters
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
            yield from tree(path, prefix=prefix + extension)


if __name__ == '__main__':
    pass

