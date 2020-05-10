"""Module to test online sources parsers."""
import pytest
from geniepy.datamgmt.parsers import BaseParser, ClassifierParser
import tests.testdata as td
from tests.resources.mock import TEST_CHUNKSIZE


VALID_DF = td.CLSFR_VALID_DF
INVALID_DF = td.CLSFR_INVALID_DF


class TestClassifierParser:
    """Pytest CTD Parser class."""

    parser: BaseParser = ClassifierParser()

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

    def test_parse_not_impl(self):
        """Parse method should not be implemented in classifier parser."""
        with pytest.raises(NotImplementedError):
            self.parser.parse(None)

    def test_fetch_not_impl(self):
        """Fetch method should not be implemented in classifier parser."""
        with pytest.raises(NotImplementedError):
            self.parser.fetch(TEST_CHUNKSIZE)
