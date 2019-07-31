import shlex

import pytest
from click.testing import CliRunner

from src.cli import Workflow


@pytest.fixture
def input_fixture_wrapper():
    def input_fixture(input_str: str = 'j\nk\nq\n'):
        return input_str
    return input_fixture


def test_e2e_happy_path_cli_webpage_binary(input_fixture_wrapper):
    """Test happy path for cli webpage binary training set command"""
    runner = CliRunner()

    with runner.isolated_filesystem():
        result = runner.invoke(
            workflow, 
            shlex.split('webpage binary --file ./files/webpage-binary-two-line.csv'),
            input=input_fixture_wrapper()
        )
        assert result.exit_code == 0, result.output
        assert result.output == 'foo=j\nfoo=k\nfoo=q\n'

