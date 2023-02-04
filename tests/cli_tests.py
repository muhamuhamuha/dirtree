import pytest

import cli

from typing import Any


@pytest.mark.parametrize(
    'argvs, expected', [
        # nothing supplied
        (
            [],
            {
                'project_path': '.',
                'view_exclusions': False,
                'modify_exclusion': None,
                'subtract_exclusion': None,
                'add_exclusions': None,
                'delete_all_exclusions': False,
            }
        ),
        (['-v'], {'view_exclusions': True}),
        (
            ['-m', '0:hi', '--modify-exclusion', '1:goodbye'],
            {
                'view_exclusions': False,
                'modify_exclusion': ['0:hi', '1:goodbye']
            }
        ),
        (
            ['-s', '0', '--subtract-exclusion', '22'],
            {'subtract_exclusion': [0, 22]}
        ),
        (['--add-exclusions', 'hello'], {'add_exclusions': ['hello']}),
        (['--add-exclusions', 'hi', 'hi2'], {'add_exclusions': ['hi', 'hi2']}),
        (
            ['-a', 'these', 'are', 'the', 'droids'],
            {'add_exclusions': ['these', 'are', 'the', 'droids']}
        ),
        (['-d'], {'delete_all_exclusions': True}),
    ]
)
def test_compile_cli(argvs: list[str], expected: dict[str, Any]):
    parser = cli.compile_cli()
    inputs = parser.parse_args(argvs)

    for attr, expectation in expected.items():
        assert getattr(inputs, attr) == expectation

