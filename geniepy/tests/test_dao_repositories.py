"""Module to test data access object repositories."""
import pytest
import tests.testdata as td
from geniepy.datamgmt.daorepositories import BaseDaoRepo, SqlDaoRepo
import geniepy.datamgmt.daorepositories as dr
from geniepy.errors import DaoError


class TestDaoRepo:
    """PyTest collector test class."""

    dao_repo: BaseDaoRepo = SqlDaoRepo(
        "sqlite://", dr.CTD_TABLE_NAME, dr.CTD_DAO_SCHEMA
    )

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

    @pytest.mark.parametrize("payload", td.CTD_VALID_DF)
    def test_query(self, payload):
        """Query valid record."""
        # Try to create records in db for test if don't exist
        try:
            self.dao_repo.save(payload)
        except DaoError:
            pass
        # Attempt to retrieve record
        digest = payload.Digest[0]
        query_str = f"SELECT * FROM {self.dao_repo.tablename} WHERE Digest='{digest}';"
        generator = self.dao_repo.query(query=query_str)
        chunk = next(generator)
        assert chunk.equals(payload)

    def test_query_non_existent(self):
        """Query non-existent record should return empty."""
        # Attempt to retrieve record
        digest = "INVALID DIGEST"
        query_str = f"SELECT * FROM {self.dao_repo.tablename} WHERE Digest='{digest}';"
        generator = self.dao_repo.query(query=query_str)
        # Make sure generator doesn't return anything since no records in database
        with pytest.raises(StopIteration):
            next(generator)

    @pytest.mark.parametrize("chunksize", [1, 2, 3, 4])
    def test_generator_chunk(self, chunksize):
        """Query all by chunk."""
        # Try to fill database, in case is empty
        for record in td.CTD_VALID_DF:
            try:
                self.dao_repo.save(record)
            except DaoError:
                pass
        # Get all records in database
        query_str = f"SELECT * FROM {self.dao_repo.tablename};"
        generator = self.dao_repo.query(query=query_str, chunksize=chunksize)
        # Make sure number generator provides df of chunksize each iteration
        result_df = next(generator)
        assert result_df.Digest.count() == chunksize
