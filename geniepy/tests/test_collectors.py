"""Module to test collectors."""
import pytest
from geniepy.datamgmt.collectors import CtdCollector
from geniepy.errors import SchemaError
import tests.testdata as td


class TestCtdCollector:
    """PyTest collector test class."""

    collector = CtdCollector()

    def test_constructor(self):
        """Ensure scraper obj constructed successfully."""
        assert self.collector is not None

    @pytest.mark.parametrize("payload", td.CTD_INVALID_DF)
    def test_save_invalid_df(self, payload):
        """Test save invalid dataframe to collector's DAO."""
        with pytest.raises(SchemaError):
            self.collector.save(payload)
