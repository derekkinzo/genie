
"""Module to test online sources parsers."""
import pytest
from geniepy.datamgmt.parsers import BaseParser, PubMedParser
from geniepy.errors import ParserError
import tests.testdata as td
from tests.resources.mock import MockPubMedScraper
from geniepy.datamgmt.scrapers import PubMedScraper
from geniepy.datamgmt.daos import BaseDao, PubMedDao
from geniepy.errors import SchemaError
import tests.testdata as td
from tests.resources.mock import MockPubMedScraper
from tests.resources.mock import TEST_CHUNKSIZE
import geniepy.datamgmt.repositories as dr
from geniepy.datamgmt.tables import PUBMED_PROPTY
from geniepy.errors import DaoError



VALID_DF = td.PUBMED_VALID_DF
INVALID_DF = td.PUBMED_INVALID_DF


class TestPubMedParser:
    """Pytest CTD Parser class."""

    test_repo = dr.SqlRepository("sqlite:///pubmed.db", PUBMED_PROPTY)
    test_dao: BaseDao = PubMedDao(test_repo)

    parser: BaseParser = PubMedParser()
    parser.scraper = PubMedScraper()
    

    def test_parse_valid(self):
        """Test parsing valid recrods."""
        chunksize = 3
        scrape_gen = self.parser.scraper.scrape(chunksize=chunksize)
        xml_articles = next(scrape_gen)
        parsed_df = self.parser.parse(xml_articles)
        assert parsed_df.shape[0] == chunksize

    @pytest.mark.parametrize("chunksize", [*range(1, 3)])
    def test_download(self, chunksize):
        """
        Test download method for historical data.

        The first time update is called (databases are still empty), it should download
        all historical info from online sources.
        """
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