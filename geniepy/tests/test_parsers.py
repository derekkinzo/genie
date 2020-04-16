"""Module to test online sources parsers."""
import pandas as pd
import pytest
from geniepy.datamgmt.parsers import BaseParser, CtdParser
from geniepy.errors import SchemaError


class TestCtdParser:
    """Pytest CTD Parser class."""

    parser: BaseParser = CtdParser()
    invalid_ctd_df = [None, pd.DataFrame({"invalid": [1, 2]})]
    valid_ctd_df = [
        pd.DataFrame(
            {
                "GeneSymbol": ["11-BETA-HSD3"],
                "GeneID": [100174880],
                "DiseaseName": ["Abnormalities, Drug-Induced"],
                "DiseaseID": ["D000014"],
                "PubMedIDs": [22659286],
            }
        )
    ]

    def test_constructor(self):
        """Ensure scraper obj constructed successfully."""
        assert self.parser is not None

    @pytest.mark.parametrize("payload", invalid_ctd_df)
    def test_invalid_payload(self, payload):
        """Test invalid dataframe."""
        assert not self.parser.is_valid(payload)

    @pytest.mark.parametrize("payload", valid_ctd_df)
    def test_valid_payload(self, payload):
        """Test valid dataframe."""
        assert self.parser.is_valid(payload)
