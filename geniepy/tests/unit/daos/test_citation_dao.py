"""Module to test Data Access Objects."""
import pytest
from geniepy.datamgmt.daos import BaseDao, CitationDao
from geniepy.errors import SchemaError
from geniepy.errors import DaoError
import geniepy.datamgmt.repositories as dr
from geniepy.datamgmt.tables import CITATION_PROPTY
from geniepy.datamgmt.parsers import CitationParser
from geniepy.datamgmt.scrapers import CitationScraper
from pandas import DataFrame
# import tests.testdata as td
# from tests.resources.mock import MockCtdScraper
# from tests.resources.mock import TEST_CHUNKSIZE
from pandas._testing import assert_frame_equal


class TestCitationDao:
    """PyTest data access object test class."""

    test_repo = dr.SqlRepository("sqlite://", CITATION_PROPTY)
    test_dao: BaseDao = CitationDao(test_repo)
    
    citation_scraper = CitationScraper()
    CitationParser.scraper = citation_scraper

    df_columns = ["pmid", "citation_count", "citation_pmid"]
    mock_data_1 = [[1, 5, "31264500,30186270,29460824,28851427,27574557"]]
    mock_data_10 = [
        [1 ,5, "31264500,30186270,29460824,28851427,27574557"],
        [2 ,4, "31435170,26259654,26140007,25548608"],
        [3 ,4, "27767123,25624746,24775716,12463"],
        [5 ,2, "3380793,1061139"],
        [6 ,2, "28601826,26668515"],
        [7 ,5, "27705745,6713511,2858585,41093,18246"],
        [8 ,4, "32005835,31664040,25584359,9224641"],
        [11 ,2, "391006,15249"],
        [12 ,6, "29576450,28944107,28487673,12023879,6249261,6128974"],
        [16 ,4, "23687416,6814425,1008838,35157"]]    

    def test_constructor(self):
        """Ensure obj constructed successfully."""
        assert self.test_dao is not None

    def read_record(self, pmid):
        """Read record(s) from database (tests helper method)."""
        query_str = self.test_dao.query_pkey(pmid)
        generator = self.test_dao.query(query_str, 5)
        return generator        

    def test_save_invalid_df(self):
        """Test save invalid dataframe to dao's repository."""
        mock_df = DataFrame()
        with pytest.raises(SchemaError):
            self.test_dao.save(mock_df)

    def test_save_valid_df(self):
        """Test save valid dataframe to dao's repo doesn't raise error."""
        mock_df = DataFrame(self.mock_data_1)
        mock_df.columns = self.df_columns        
        self.test_dao.save(mock_df)

    def test_tablename(self):
        """Test tablename property."""
        expected = "pubmed_citation"
        actual = self.test_dao.tablename
        assert actual == expected

    def test_query(self):
        """Query valid record."""
        # Start with empty table
        self.test_dao.purge()
        # create mock data frame
        mock_df = DataFrame(self.mock_data_1)
        mock_df.columns = self.df_columns        

        # Try to create records in db for test if don't exist
        try:
            self.test_dao.save(mock_df)
        except DaoError:
            pass
        # Attempt to retrieve record
        pmid = mock_df.pmid[0]
        generator = self.read_record(pmid)
        chunk = next(generator)
        assert chunk.equals(mock_df)

    def test_query_non_existent(self):
        """Query non-existent record should return empty."""
        # Attempt to retrieve record
        pmid = 0
        generator = self.read_record(pmid)
        # Make sure generator doesn't return anything since no records in database
        with pytest.raises(StopIteration):
            next(generator)

    def test_purge(self):
        """Test delete all records from repository."""
        TEST_CHUNKSIZE = 5

        # create mock data frame
        mock_df = DataFrame(self.mock_data_1)
        mock_df.columns = self.df_columns

        # Try to fill database, in case is empty
        try:
            self.test_dao.save(mock_df)
        except DaoError:
            pass
        # Delete all records
        self.test_dao.purge()
        # Make sure no records left
        generator = self.test_dao.query(self.test_dao.query_all, TEST_CHUNKSIZE)
        # generator shouldn't return anything since no records in database
        with pytest.raises(StopIteration):
            next(generator)
        # Test building and reading from table again, make sure still functional
        self.test_query()

    def test_query_chunksize(self):
        chunksize = 5

        # create mock data frame
        mock_df = DataFrame(self.mock_data_10)
        mock_df.columns = self.df_columns

        """Query all by chunk."""
        # Try to fill database, in case is empty
        for i in range(0,mock_df.pmid.count()):
            try:
                self.test_dao.save(mock_df[i:i+1])
            except DaoError:
                pass
        # Get all records in database
        generator = self.test_dao.query(self.test_dao.query_all, chunksize)
        # Make sure number generator provides df of chunksize each iteration
        result_df = next(generator)
        assert result_df.pmid.count() == chunksize

    def test_download(self):
        """
        Test download method for historical data.

        The first time update is called (databases are still empty), it should download
        all historical info from online sources.
        """
        TEST_CHUNKSIZE = 5
        chunksize = 5
        # Make sure dao's database is empty
        self.test_dao.purge()
        generator = self.test_dao.query(self.test_dao.query_all, TEST_CHUNKSIZE)
        # Generator should not return anything since database should be empty
        with pytest.raises(StopIteration):
            next(generator)
        # Call download method to update database with data from online sources
        self.test_dao.download(chunksize)
        # Read entire table
        generator = self.test_dao.query(self.test_dao.query_all, chunksize)
        # Generator should return values
        result_df = next(generator)
        assert not result_df.empty
