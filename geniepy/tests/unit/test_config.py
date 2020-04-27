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
    expected = 10
    actual = config.get_chunksize()
    assert actual == expected


def test_get_dao_mgr_invalid_path():
    """Test get valid daomgr raises config error without valid path."""
    with pytest.raises(ConfigError):
        config.get_daomgr()


def test_get_clsfr():
    """Test getting classifiers."""
    assert config.get_classmgr() is not None
