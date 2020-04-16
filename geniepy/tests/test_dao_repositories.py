"""Module to test data access object repositories."""
import pandas as pd
import pytest
from geniepy.datamgmt.daorepositories import BaseDaoRepository
from geniepy.exceptions import SchemaError


class TestSqliteCollector:
    """PyTest collector test class."""

    dao_repo: BaseDaoRepository = None
    invalidDF: pd.DataFrame = pd.DataFrame({"invalid": [1, 2]})

    def test_constructor(self):
        """Ensure scraper obj constructed successfully."""
        assert self.dao_repo is not None

    @pytest.mark.parametrize("payload", [None, invalidDF])
    def test_save_invalid_df(self, payload):
        """Test save invalid dataframe to collector's DAO."""
        with pytest.raises(SchemaError):
            self.dao_repo.save(payload)
