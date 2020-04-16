"""Module to test online sources parsers."""
import pandas as pd
import pytest
from geniepy.datamgmt.parsers import BaseParser
from geniepy.exceptions import SchemaError


class TestSqliteCollector:
    """PyTest collector test class."""

    parser: BaseParser = None
    # invalidDF: pd.DataFrame = pd.DataFrame({"invalid": [1, 2]})

    def test_constructor(self):
        """Ensure scraper obj constructed successfully."""
        assert self.parser is not None

    # @pytest.mark.parametrize("payload", [None, invalidDF])
    # def test_save_invalid_df(self, payload):
    #     """Test save invalid dataframe to collector's DAO."""
    #     with pytest.raises(SchemaError):
    #         self.dao_repo.save(payload)
