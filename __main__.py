from pathlib import Path
from pprint import pprint

import dirtree
from cli import cli


def main() -> None:
    opt = cli()

    excl = dirtree.modify_exclusions(dirtree.EXCLUSIONS, opt.modify_exclusion)

    subtractions = opt.subtract_exclusion or []
    for sub in subtractions:
        excl.pop(sub)

    excl = dirtree.add_exclusions(excl, opt.add_exclusions)
    if opt.view_exclusions:
        pprint(excl)


    for tree in dirtree.dirtree(Path(opt.project_path), '|'.join(excl.values())):
        print(tree)


if __name__ == '__main__':
    main()

