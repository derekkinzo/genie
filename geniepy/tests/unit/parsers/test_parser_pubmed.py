"""Module to test online sources parsers."""
import pytest
from geniepy.datamgmt.parsers import BaseParser, PubMedParser
from geniepy.datamgmt.scrapers import PubMedScraper
from geniepy.errors import ParserError
import tests.testdata as td
from tests.resources.mock import MockPubMedScraper


VALID_DF = td.PUBMED_VALID_DF
INVALID_DF = td.PUBMED_INVALID_DF


class TestPubMedParser:
    """Pytest CTD Parser class."""

    parser: BaseParser = PubMedParser()
    pubmed_scraper = PubMedScraper()
    parser.scraper = pubmed_scraper

    def test_constructor(self):
        """Ensure scraper obj constructed successfully."""
        assert self.parser is not None

    def test_parse_valid(self):
        """Test parsing valid recrods."""
        chunksize = 3
        scrape_gen = self.parser.scraper.scrape(chunksize=chunksize)
        xml_articles = next(scrape_gen)
        parsed_df = self.parser.parse(xml_articles)
        assert parsed_df.shape[0] == chunksize

