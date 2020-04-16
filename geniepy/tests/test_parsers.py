"""Module to test online sources parsers."""
import pandas as pd
import pytest
from geniepy.datamgmt.parsers import BaseParser, CtdParser
from geniepy.errors import SchemaError
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
        assert not self.parser.is_valid(payload)

    @pytest.mark.parametrize("payload", td.CTD_VALID_DF)
    def test_valid_payload(self, payload):
        """Test valid dataframe."""
        assert self.parser.is_valid(payload)
