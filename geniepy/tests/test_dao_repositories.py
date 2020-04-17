"""Module to test data access object repositories."""
import pytest
import tests.testdata as td
from geniepy.datamgmt.daorepositories import BaseDaoRepo, SqlDaoRepo
from geniepy.errors import DaoError


class TestDaoRepo:
    """PyTest collector test class."""

    dao_repo: BaseDaoRepo = SqlDaoRepo("sqlite://", "ctd")

    def test_constructor(self):
        """Ensure scraper obj constructed successfully."""
        assert self.dao_repo is not None

    @pytest.mark.parametrize("payload", td.CTD_INVALID_DAO)
    def test_save_invalid_df(self, payload):
        """Test save invalid dataframe to collector's DAO."""
        with pytest.raises(DaoError):
            self.dao_repo.save(payload)

    @pytest.mark.parametrize("payload", td.CTD_VALID_DF)
    def test_save_valid_df(self, payload):
        """Attempt to save dataframe with valid schema."""
        self.dao_repo.save(payload)  # Don't expect to return anything

    # Query valid record
    @pytest.mark.parametrize("payload", td.CTD_VALID_DF)
    def test_query(self, payload):
        """Attempt to save dataframe with valid schema."""
        # Try to create records in db for test if don't exist
        try:
            self.test_save_valid_df(payload)
        except DaoError:
            pass
        # Attempt to retrieve record
        digest = payload.Digest[0]
        query_str = f"SELECT * FROM {self.dao_repo.tablename} WHERE Digest='{digest}';"
        generator = self.dao_repo.query(query=query_str)
        for df in generator:
            assert df.equals(payload)

    # Query non-existent record should return empty

    # Query all by chunk
