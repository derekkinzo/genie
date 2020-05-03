"""Integration tests of Pubtator - Gene data."""
import pytest
from pathlib import Path
from geniepy.datamgmt.scrapers import PubtatorGeneScraper
from tests.resources.mock import TEST_CHUNKSIZE


FTP_URL_SAMPLE = (
    "ftp://ftp.ncbi.nlm.nih.gov/pub/lu/PubTatorCentral/gene2pubtatorcentral.gz"
)


@pytest.mark.slow_integration_test
class TestPubtatorGeneScraper:
    """Test pubtator gene scraper."""

    def test_download():
        """Test downloding data."""
        pbs = PubtatorGeneScraper()
        pbs.clean_up()
        pbs.download()
        assert Path.exists(pbs.PUBTATOR_CSV_NAME)
        assert Path.exists(pbs.PUBTATOR_GZIP_NAME)

    def test_cleanup():
        """Test deleting generated files."""
        pbs = PubtatorGeneScraper()
        if not Path.exists(pbs.PUBTATOR_CSV_NAME):
            Path(pbs.PUBTATOR_CSV_NAME).touch()
        pbs.clean_up()
        assert not Path.exists(pbs.PUBTATOR_CSV_NAME)

    def test_scrape():
        """Test scraping data from pubtator-gene."""
        pbs = PubtatorGeneScraper()
        gen = pbs.scrape(TEST_CHUNKSIZE)
        df = next(gen)
        assert df.shape[0] == TEST_CHUNKSIZE
