import shlex

import pytest
import click
from click.testing import CliRunner
# from src.training_tagger.cli import workflow

@pytest.fixture
def input_fixture_wrapper():
    def input_fixture(input_str: str = 'j\nk\nq\n'):
        return input_str
    return input_fixture

@click.command()
def my_cmd():
    while True:
        input_str = input()
        click.echo(f'foo={input_str}')
        if input_str == 'q':
            break


def test_e2e_happy_path_cli_webpage_binary(input_fixture_wrapper):
    """Test happy path for cli webpage binary training set command"""
    runner = CliRunner()
    result = runner.invoke(
        my_cmd, 
        input=input_fixture_wrapper()
    )
    #shlex.split('webpage binary ./files/webpage-binary-two-line.csv'),
    assert result.exit_code == 0
    assert result.output == 'foo=j\nfoo=k\nfoo=q\n'

