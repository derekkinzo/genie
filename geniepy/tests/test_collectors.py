"""Module to test collectors."""
import pandas as pd
import pytest
from geniepy.datamgmt.collectors import CtdCollector
from geniepy.errors import SchemaError


class TestCtdCollector:
    """PyTest collector test class."""

    collector = CtdCollector()
    invalid_ctd_df = [None, pd.DataFrame({"invalid": [1, 2]})]
    valid_ctd_df = [{}]

    def test_constructor(self):
        """Ensure scraper obj constructed successfully."""
        assert self.collector is not None

    @pytest.mark.parametrize("payload", invalid_ctd_df)
    def test_save_invalid_df(self, payload):
        """Test save invalid dataframe to collector's DAO."""
        with pytest.raises(SchemaError):
            self.collector.save(payload)
