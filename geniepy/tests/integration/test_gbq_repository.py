"""Pytest module to test Google BigQuery Repository."""
import os
import pytest
import tests.testdata as td
import geniepy.datamgmt.repositories as dr
from geniepy.datamgmt.tables import PUBMED_PROPTY, CTD_PROPTY, CLSFR_PROPTY
from geniepy.errors import DaoError
from tests import get_test_output_path
from tests.resources.mock import TEST_CHUNKSIZE


# Name of credential file (assumed to be in tests/tests_output dir)
credentials_file = "genie_credentials.json"
credpath = os.path.join(get_test_output_path(), credentials_file)
# Google BigQuery Project Name
projname = "genie-275215"
dataset = "test"


VALID_DF = td.PUBMED_VALID_DF
INVALID_SCHEMA = td.PUBMED_INVALID_SCHEMA


@pytest.mark.slow_integration_test
class TestGbqRepository:
    """Test db.pubmed_repository on Google BigQuery."""

    pubmed_repo: dr.BaseRepository = None
    ctd_repo: dr.BaseRepository = None
    clsfr_repo: dr.BaseRepository = None

    @classmethod
    def setup_class(cls):
        """Initialize GBQ.pubmed_repo."""
        cls.pubmed_repo = dr.GbqRepository(projname, PUBMED_PROPTY, dataset, credpath)
        cls.ctd_repo = dr.GbqRepository(projname, CTD_PROPTY, dataset, credpath)
        cls.clsfr_repo = dr.GbqRepository(projname, CLSFR_PROPTY, dataset, credpath)

    def test_constructor(self):
        """Test constructing object."""
        assert self.pubmed_repo is not None


    @pytest.mark.parametrize("payload", INVALID_SCHEMA)
    def test_save_invalid_df(self, payload):
        """Test save invalid dataframe to dao's DAO."""
        with pytest.raises(DaoError):
            self.pubmed_repo.save(payload)

    @pytest.mark.parametrize("payload", VALID_DF)
    def test_save_valid_df(self, payload):
        """Attempt to save dataframe with valid schema."""
        self.pubmed_repo.save(payload)  # Don't expect to return anything

    def test_query(self):
        """Query valid record."""
        payload = VALID_DF[0]
        # Start with empty table
        self.pubmed_repo.delete_all()
        # Try to create records in db for test if don't exist
        try:
            self.pubmed_repo.save(payload)
        except DaoError:
            pass
        # Attempt to retrieve record
        pmid = payload.pmid[0]
        query_str = f"SELECT * FROM {self.pubmed_repo.tablename} WHERE pmid={pmid};"
        generator = self.pubmed_repo.query(query_str, TEST_CHUNKSIZE)
        chunk = next(generator)
        assert chunk.pmid.equals(payload.pmid)

    def test_invalid_query(self):
        """Test making invalid queries."""
        query_str = "Invalid"
        with pytest.raises(DaoError):
            next(self.pubmed_repo.query(TEST_CHUNKSIZE, query=query_str))

    def test_query_non_existent(self):
        """Query non-existent record should return empty."""
        # Attempt to retrieve record
        pmid = 0
        query_str = f"SELECT * FROM {self.pubmed_repo.tablename} WHERE pmid={pmid};"
        generator = self.pubmed_repo.query(TEST_CHUNKSIZE, query=query_str)
        # Make sure generator doesn't return anything since no matching records
        with pytest.raises(StopIteration):
            next(generator)

    @pytest.mark.parametrize("chunksize", [1, 2, 3])
    def test_generator_chunk(self, chunksize):
        """Query all by chunk."""
        # Start with empty table
        self.pubmed_repo.delete_all()
        # Try to fill database, in case is empty
        for record in VALID_DF:
            try:
                self.pubmed_repo.save(record)
            except DaoError:
                pass
        # Get all records in database
        generator = self.pubmed_repo.query(chunksize=chunksize)
        # Make sure number generator provides df of chunksize each iteration
        result_df = next(generator)
        assert result_df.pmid.count() == chunksize

    def test_delete_all(self):
        """Test delete all records from.pubmed_repository."""
        # Try to fill database, in case is empty
        for record in VALID_DF:
            try:
                self.pubmed_repo.save(record)
            except DaoError:
                pass
        # Delete all records
        self.pubmed_repo.delete_all()
        # Make sure no records left
        generator = self.pubmed_repo.query(TEST_CHUNKSIZE)
        # generator shouldn't return anything since no records in database
        with pytest.raises(StopIteration):
            next(generator)
        # Test saving and reading from table again, make sure still functional
        self.pubmed_repo.save(VALID_DF[0])
        generator = self.pubmed_repo.query(TEST_CHUNKSIZE)
        # Generator should return value
        next(generator)
