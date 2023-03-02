import pytest
import ChocAn

@pytest.fixture
def setup():
    terminal = ChocAn.Terminal()
    return terminal