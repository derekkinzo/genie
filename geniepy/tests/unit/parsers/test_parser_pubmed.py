"""Module to test online sources parsers."""
import pytest
from geniepy.datamgmt.parsers import BaseParser, PubMedParser
from geniepy.errors import ParserError
import tests.testdata as td
from tests.resources.mock import MockPubMedScraper


VALID_DF = td.PUBMED_VALID_DF
INVALID_DF = td.PUBMED_INVALID_DF


class TestPubMedParser:
    """Pytest CTD Parser class."""

    parser: BaseParser = PubMedParser()
    mock_scraper = MockPubMedScraper()
    parser.scraper = mock_scraper

    def test_constructor(self):
        """Ensure scraper obj constructed successfully."""
        assert self.parser is not None

    @pytest.mark.parametrize("payload", INVALID_DF)
    def test_invalid_payload(self, payload):
        """Test invalid dataframe."""
        # Should return list with errors
        assert self.parser.validate(payload)

    @pytest.mark.parametrize("payload", VALID_DF)
    def test_valid_payload(self, payload):
        """Test valid dataframe."""
        # Should return empty list
        assert not self.parser.validate(payload)

    def test_parse_valid(self):
        """Test parsing valid recrods."""
        chunksize = 3
        scrape_gen = self.parser.scraper.scrape(chunksize=chunksize)
        xml_articles = next(scrape_gen)
        parsed_df = self.parser.parse(xml_articles)
        assert parsed_df.shape[0] == chunksize

    def test_parse_invalid_file(self):
        """Attempt to parse invalid data."""
        with pytest.raises(ParserError):
            self.parser.parse("invalid xml")
