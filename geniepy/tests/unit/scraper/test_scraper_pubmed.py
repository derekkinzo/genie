"""Module to test PubMed scraper."""
import pytest
from geniepy.datamgmt.scrapers import PubMedScraper

class TestPubMedScraper:
    """Pytest PubMed Scraper class."""

    scraper: PubMedScraper = PubMedScraper()

    def test_constructor(self):
        """Ensure scraper obj constructed successfully."""
        assert self.scraper is not None

    @pytest.mark.parametrize('chunksize', [1, 100, 1000])
    def test_scrape(self, chunksize):
        """Test scraping valid recrods."""
        scrape_gen = self.scraper.scrape(chunksize=chunksize)
        articles = next(scrape_gen)
        assert len(articles) == chunksize

