"""Module to test data access object repositories."""
import pytest
import tests.testdata as td
from geniepy.datamgmt.repositories import BaseRepository, SqlRepository
import geniepy.datamgmt.repositories as dr
from geniepy.errors import DaoError

INVALID_DAO = td.CTD_INVALID_DAO
VALID_DF = td.CTD_VALID_DF
INVALID_DF = td.CTD_INVALID_DF


class TestSqlCtdRepository:
    """PyTest dao test class."""

    repo: BaseRepository = SqlRepository(
        "sqlite://", dr.CTD_TABLE_NAME, dr.CTD_DAO_TABLE
    )

    def test_constructor(self):
        """Ensure scraper obj constructed successfully."""
        assert self.repo is not None

    @pytest.mark.parametrize("payload", INVALID_DAO)
    def test_save_invalid_df(self, payload):
        """Test save invalid dataframe to dao's DAO."""
        with pytest.raises(DaoError):
            self.repo.save(payload)

    @pytest.mark.parametrize("payload", VALID_DF)
    def test_save_valid_df(self, payload):
        """Attempt to save dataframe with valid schema."""
        self.repo.save(payload)  # Don't expect to return anything

    @pytest.mark.parametrize("payload", VALID_DF)
    def test_query(self, payload):
        """Query valid record."""
        # Start with empty table
        self.repo.delete_all()
        # Try to create records in db for test if don't exist
        try:
            self.repo.save(payload)
        except DaoError:
            pass
        # Attempt to retrieve record
        digest = payload.Digest[0]
        query_str = f"SELECT * FROM {self.repo.tablename} WHERE Digest='{digest}';"
        generator = self.repo.query(query=query_str)
        chunk = next(generator)
        assert chunk.equals(payload)

    def test_query_non_existent(self):
        """Query non-existent record should return empty."""
        # Attempt to retrieve record
        digest = "INVALID DIGEST"
        query_str = f"SELECT * FROM {self.repo.tablename} WHERE Digest='{digest}';"
        generator = self.repo.query(query=query_str)
        # Make sure generator doesn't return anything since no matching records
        with pytest.raises(StopIteration):
            next(generator)

    @pytest.mark.parametrize("chunksize", [1, 2, 3, 4])
    def test_generator_chunk(self, chunksize):
        """Query all by chunk."""
        # Start with empty table
        self.repo.delete_all()
        # Try to fill database, in case is empty
        for record in VALID_DF:
            try:
                self.repo.save(record)
            except DaoError:
                pass
        # Get all records in database
        generator = self.repo.query(chunksize=chunksize)
        # Make sure number generator provides df of chunksize each iteration
        result_df = next(generator)
        assert result_df.Digest.count() == chunksize

    def test_delete_all(self):
        """Test delete all records from repository."""
        # Try to fill database, in case is empty
        for record in VALID_DF:
            try:
                self.repo.save(record)
            except DaoError:
                pass
        # Delete all records
        self.repo.delete_all()
        # Make sure no records left
        generator = self.repo.query()
        # generator shouldn't return anything since no records in database
        with pytest.raises(StopIteration):
            next(generator)
        # Test saving and reading from table again, make sure still functional
        self.repo.save(VALID_DF[0])
        generator = self.repo.query()
        # Generator should return value
        next(generator)
