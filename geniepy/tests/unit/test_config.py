"""Test package configuration & yaml files."""
from pathlib import Path
import pytest
import geniepy.config as config
from geniepy.errors import ConfigError
from tests import get_resources_path

TEST_CONFIG_NAME = "testconfig.yaml"
TEST_CONFIG_PATH = Path(get_resources_path()).resolve().joinpath(TEST_CONFIG_NAME)

# Override default config path for tests
config.CONFIG_PATH = TEST_CONFIG_PATH


def test_chunksize():
    """Test retrieving chunksize."""
    expected = 100000
    actual = config.get_chunksize()
    assert actual == expected


def test_get_clsfr():
    """Test getting classifiers."""
    assert config.get_classmgr() is not None
