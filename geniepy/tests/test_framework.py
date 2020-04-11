"""Basic pytest test to ensure testing framework is working."""
import pytest


def test_pytest():
    """Test is pytest is working."""
    with pytest.raises(Exception):
        raise Exception
    assert True
