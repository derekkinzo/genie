"""Module to test online sources parsers."""
import pytest
from geniepy.datamgmt.parsers import BaseParser, CtdParser
from geniepy.errors import ParserError
from tests.resources.mock import MockCtdScraper
import tests.testdata as td


class TestCtdParser:
    """Pytest CTD Parser class."""

    parser: BaseParser = CtdParser()
    mock_scraper = MockCtdScraper()
    parser.scraper = mock_scraper

    def test_constructor(self):
        """Ensure scraper obj constructed successfully."""
        assert self.parser is not None

    @pytest.mark.parametrize("payload", td.CTD_INVALID_DF)
    def test_invalid_payload(self, payload):
        """Test invalid dataframe."""
        # Should return list with errors
        assert self.parser.validate(payload)

    @pytest.mark.parametrize("payload", td.CTD_VALID_DF)
    def test_valid_payload(self, payload):
        """Test valid dataframe."""
        # Should return empty list
        assert not self.parser.validate(payload)

    # TODO Test Parse Method
    def test_parse_valid(self):
        """Test parsing valid recrods."""
        mock_scraper = MockCtdScraper()
        scrape_gen = mock_scraper.scrape()
        self.parser.parse(next(scrape_gen))

    def test_parse_invalid_file(self):
        """Attempt to parse invalid data."""
        with pytest.raises(ParserError):
            self.parser.parse("invalid csv")

    def test_parse_invalid_df(self):
        """Attempt to parse invalid/incomplete dataframe."""
        mock_scraper = MockCtdScraper()
        mock_scraper.filename = "sample_corrupt_ctd_db.csv"
        scrape_gen = mock_scraper.scrape()
        with pytest.raises(ParserError):
            self.parser.parse(next(scrape_gen))

    def test_fetch(self):
        """Test parser fetch."""
        gen_data = self.parser.fetch()
        data = next(gen_data)
        assert data is not None
