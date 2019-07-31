import pytest

from src.simple_tagger import WebpageBinaryTrainingSet


@pytest.fixture
def webpage_binary_training_set():
    filename = 'files/webpage_binary_training_set_two_rows.csv'
    return WebpageBinaryTrainingSet(filename=filename)


def test_ut_webpage_binary_init(webpage_binary_training_set):
    """Test creating WebpageBinaryTrainingSet object"""
    assert isinstance(webpage_binary_training_set, WebpageBinaryTrainingSet)


