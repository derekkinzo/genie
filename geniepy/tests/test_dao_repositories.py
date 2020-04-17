"""Module to test data access object repositories."""
import pytest
import tests.testdata as td
from geniepy.datamgmt.daorepositories import BaseDaoRepo, SqliteDaoRepo
from geniepy.errors import DaoError


class TestDaoRepo:
    """PyTest collector test class."""

    dao_repo: BaseDaoRepo = SqliteDaoRepo("sqlite://", "ctd")

    def test_constructor(self):
        """Ensure scraper obj constructed successfully."""
        assert self.dao_repo is not None

    @pytest.mark.parametrize("payload", td.CTD_INVALID_DAO)
    def test_save_invalid_df(self, payload):
        """Test save invalid dataframe to collector's DAO."""
        with pytest.raises(DaoError):
            self.dao_repo.save(payload)

    # @pytest.mark.parametrize("payload", td.CTD_VALID_DF)
    # def test_save_valid_df(self, payload):
    #     """Attempt to save dataframe with valid schema."""
    #     self.dao_repo.save(payload)  # Don't expect to return anything
