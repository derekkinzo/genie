"""Test base classifier class."""
from tests.resources.mock import MockClsfr


def test_constructor():
    """Construct mock classifier."""
    classifier = MockClsfr()
    assert classifier is not None
