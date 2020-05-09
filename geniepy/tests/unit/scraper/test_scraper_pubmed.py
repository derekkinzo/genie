"""Module to test PubMed scraper."""
import pytest
from geniepy.datamgmt.scrapers import PubMedScraper


class TestPubMedScraper:
    """Pytest PubMed Scraper class."""

    scraper: PubMedScraper = PubMedScraper()

    def test_constructor(self):
        """Ensure scraper obj constructed successfully."""
        assert self.scraper is not None

    @pytest.mark.slow_integration_test
    @pytest.mark.parametrize("chunksize", [1, 10, 100])
    def test_scrape_update(self, chunksize):
        """Test scraping valid recrods -- for Daily Update dataset."""
        scrape_gen = self.scraper.scrape(chunksize=chunksize)
        articles = next(scrape_gen)
        assert len(articles) == chunksize

    @pytest.mark.slow_integration_test
    @pytest.mark.parametrize("chunksize", [1, 10, 100])
    def test_scrape_baseline(self, chunksize):
        """Test scraping valid recrods -- for Baselines dataset."""
        scrape_gen = self.scraper.scrape(chunksize=chunksize, baseline=True)
        articles = next(scrape_gen)
        assert len(articles) == chunksize
