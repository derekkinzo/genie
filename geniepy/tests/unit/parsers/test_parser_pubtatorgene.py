import tests.resources.mock as mock
from geniepy.datamgmt.parsers import PubtatorGeneParser


def test_parse():
    """Test parsing pubtator."""
    parser = PubtatorGeneParser()
    scraper = mock.MockPubtatorGeneScraper()
    gen_df = scraper.scrape(mock.TEST_CHUNKSIZE)
    parsed_df = parser.parse(next(gen_df))
    assert parsed_df.shape[0] == 1
