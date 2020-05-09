"""Module to test Data Access Objects."""
import pytest
from geniepy.datamgmt.scrapers import PubMedScraper
from geniepy.datamgmt.daos import BaseDao, PubMedDao
from geniepy.errors import SchemaError
import tests.testdata as td

# from tests.resources.mock import MockPubMedScraper
# from tests.resources.mock import TEST_CHUNKSIZE
import geniepy.datamgmt.repositories as dr
from geniepy.datamgmt.tables import PUBMED_PROPTY
from geniepy.errors import DaoError


class TestPubMedDao:
    """PyTest data access object test class."""

    TEST_CHUNKSIZE: int = 5

    test_repo = dr.SqlRepository("sqlite://", PUBMED_PROPTY)
    test_dao: BaseDao = PubMedDao(test_repo)
    # Attach mock scraper to parser for testing
    scraper: PubMedScraper = PubMedScraper()
    # pylint: disable=protected-access
    test_dao._parser.scraper = scraper

    def test_constructor(self):
        """Ensure obj constructed successfully."""
        assert self.test_dao is not None

    @pytest.mark.parametrize("payload", td.PUBMED_INVALID_DF)
    def test_save_invalid_df(self, payload):
        """Test save invalid dataframe to dao's repository."""
        with pytest.raises(SchemaError):
            self.test_dao.save(payload)

    @pytest.mark.parametrize("payload", td.PUBMED_VALID_DF)
    def test_save_valid_df(self, payload):
        """Test save valid dataframe to dao's repo doesn't raise error."""
        self.test_dao.save(payload)

    @pytest.mark.parametrize("payload", td.PUBMED_VALID_DF)
    def test_query(self, payload):
        """Query valid record."""
        # Start with empty table
        self.test_dao.purge()
        # Try to create records in db for test if don't exist
        try:
            self.test_dao.save(payload)
        except DaoError:
            pass
        # Attempt to retrieve record
        pmid = payload.pmid[0]
        generator = self.read_record(pmid)
        chunk = next(generator)
        assert chunk.equals(payload)

    def test_query_non_existent(self):
        """Query non-existent record should return empty."""
        # Attempt to retrieve record
        pmid = "INVALID pmid"
        generator = self.read_record(pmid)
        # Make sure generator doesn't return anything since no records in database
        with pytest.raises(StopIteration):
            next(generator)

    def test_purge(self):
        """Test delete all records from repository."""
        # Try to fill database, in case is empty
        for record in td.PUBMED_VALID_DF:
            try:
                self.test_dao.save(record)
            except DaoError:
                pass
        # Delete all records
        self.test_dao.purge()
        # Make sure no records left
        generator = self.test_dao.query(
            self.test_dao.query_all, TestPubMedDao.TEST_CHUNKSIZE
        )
        # generator shouldn't return anything since no records in database
        with pytest.raises(StopIteration):
            next(generator)
        # Test building and reading from table again, make sure still functional
        self.test_query(td.PUBMED_VALID_DF[0])

    @pytest.mark.parametrize("chunksize", [*range(1, len(td.PUBMED_VALID_DF) + 1)])
    def test_query_chunksize(self, chunksize):
        """Query all by chunk."""
        # Try to fill database, in case is empty
        for record in td.PUBMED_VALID_DF:
            try:
                self.test_dao.save(record)
            except DaoError:
                pass
        # Get all records in database
        generator = self.test_dao.query(self.test_dao.query_all, chunksize)
        # Make sure number generator provides df of chunksize each iteration
        result_df = next(generator)
        assert result_df.pmid.count() == chunksize

    @pytest.mark.slow_integration_test
    @pytest.mark.parametrize("chunksize", [1, 100])
    def test_download(self, chunksize):
        """
        Test download method for historical data.

        The first time update is called (databases are still empty), it should download
        all historical info from online sources.
        """
        # Make sure dao's database is empty
        self.test_dao.purge()
        generator = self.test_dao.query(
            self.test_dao.query_all, TestPubMedDao.TEST_CHUNKSIZE
        )
        # Generator should not return anything since database should be empty
        with pytest.raises(StopIteration):
            next(generator)
        # Call download method to update database with data from online sources
        self.test_dao.download(chunksize, test=True)
        # Read entire table
        generator = self.test_dao.query(self.test_dao.query_all, chunksize)
        # Generator should return values
        result_df = next(generator)
        assert not result_df.empty

    def read_record(self, pmid):
        """Read record(s) from database (tests helper method)."""
        query_str = self.test_dao.query_pkey(pmid)
        generator = self.test_dao.query(query_str, TestPubMedDao.TEST_CHUNKSIZE)
        return generator
