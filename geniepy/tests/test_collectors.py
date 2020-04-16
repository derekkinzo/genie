import pandas as pd
import pytest
from geniepy.datamgmt.collectors import CtdCollector
from geniepy.exceptions import SchemaError


class TestCtdCollector:
    """PyTest collector test class."""

    collector = CtdCollector()
    invalidDF = pd.DataFrame({"invalid": [1, 2]})

    def test_constructor(self):
        """Ensure scraper obj constructed successfully."""
        assert self.collector is not None

    @pytest.mark.parametrize("payload", [None, invalidDF])
    def test_save_invalid_df(self, payload):
        """Test save invalid dataframe to collector's DAO."""
        with pytest.raises(SchemaError):
            self.collector.save(payload)
