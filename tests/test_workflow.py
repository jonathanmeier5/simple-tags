from unittest import mock
import pytest

from src.cli import Workflow


@pytest.fixture
def dummy_training_set():
    mock = mock.MagicMock()
    return mock 


POSITIVE = 'j\n'
NEGATIVE = 'k\n'
EXIT = 'q\n'


def test_ut_workflow_handle_input_positive(dummy_training_set):
    """Ensure we can handle positive input."""
    workflow = Workflow(training_set=dummy_training_set)
    input_str = POSITIVE
    workflow.handle_input(input_str)
    assert dummy_training_set.tag_positive.called


def test_ut_workflow_handle_input_negative(dummy_training_set):
    """Ensure we can handle negative input."""
    workflow = Workflow(training_set=dummy_training_set)
    input_str = NEGATIVE
    workflow.handle_input(input_str)
    assert dummy_training_set.tag_negative.called

