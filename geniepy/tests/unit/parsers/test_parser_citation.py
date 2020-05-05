"""Module to test online sources parsers."""
import pytest
from geniepy.datamgmt.parsers import BaseParser, CitationParser
from geniepy.datamgmt.scrapers import CitationScraper
from pandas import DataFrame
from pandas._testing import assert_frame_equal


class TestCitationParser:
    """Pytest Citation Parser class."""

    parser: BaseParser = CitationParser()
    scraper: CitationScraper = CitationScraper()
    parser.scraper = scraper

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
        """Ensure scraper obj constructed successfully."""
        assert self.parser is not None

    def test_parse_withMockData1(self):
        """Ensure scraper obj constructed successfully."""
        mock_df = DataFrame(self.mock_data_1)
        mock_df.columns = self.df_columns
        assert_frame_equal(mock_df, self.parser.parse(self.mock_data_1))

    def test_parse_withMockData10(self):
        """Ensure scraper obj constructed successfully."""
        mock_df = DataFrame(self.mock_data_10)
        mock_df.columns = self.df_columns
        assert_frame_equal(mock_df, self.parser.parse(self.mock_data_10))        
                    
          
        
