import mock
import shlex

from click.testing import CliRunner
from src.training_tagger.cli import workflow

import contextmanager

@contextmanager
def input_patch(input_args: list = [])
    input_args = [''.join([x, '\n']) for x in input_args]
    with mock.patch('__builtins.input__', side_effect=input_args) as p:
        yield p
 

def test_e2e_happy_path_cli_webpage_binary(monkeypatch):
    """Test happy path for cli webpage binary training set command"""
    runner = CliRunner()
    with mock.patch('__builtins__.input', side_effect
    with input_patch(input_args=['j', 'q']) as p:
        result = runner.invoke(workflow, 
            shlex.split('webpage binary ./files/webpage-binary-two-line.csv')
            )
        assert result.output == 'foobar'
        assert result.
