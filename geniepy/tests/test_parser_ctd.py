"""Module to test online sources parsers."""
import pytest
from geniepy.datamgmt.parsers import BaseParser, CtdParser
import tests.testdata as td


class TestCtdParser:
    """Pytest CTD Parser class."""

    parser: BaseParser = CtdParser()

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

    # TODO Test Fetch Method
