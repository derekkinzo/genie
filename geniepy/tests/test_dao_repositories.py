"""Module to test data access object repositories."""
import pandas as pd
import pytest
from geniepy.datamgmt.daorepositories import BaseDaoRepo, SqliteDaoRepo
from geniepy.exceptions import SchemaError


class TestDaoRepo:
    """PyTest collector test class."""

    dao_repo: BaseDaoRepo = SqliteDaoRepo
    invalidDF: pd.DataFrame = pd.DataFrame({"invalid": [1, 2]})

    def test_constructor(self):
        """Ensure scraper obj constructed successfully."""
        assert self.dao_repo is not None
