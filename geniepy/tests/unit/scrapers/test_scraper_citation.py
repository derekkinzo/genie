"""Module to test online sources scrapers."""
import pytest
from geniepy.datamgmt.scrapers import CitationScraper

class TestCitationScraper:
    """Pytest Citation Scraper class."""

    scraper: CitationScraper = CitationScraper()

    def test_constructor(self):
        """Ensure scraper obj constructed successfully."""
        assert self.scraper is not None    
    
    def test_invalid_chunksize(self):
        """Ensure valid chunksize value."""
        with pytest.raises(ValueError):
            self.scraper.scrape(0)

    def test_invalid_startId(self):
        """Ensure valid start_id value."""
        with pytest.raises(ValueError):
            self.scraper.scrape(1, start_id='hello')
            self.scraper.scrape(1, start_id=-1)

    def test_invalid_endId(self):
        """Ensure valid end_id value."""
        with pytest.raises(ValueError):
            self.scraper.scrape(1, end_id='hello')
            self.scraper.scrape(1, end_id=-1)

    def test_invalid_range(self):
        """Ensure valid range between start_id and end_id values."""
        with pytest.raises(ValueError):
            self.scraper.scrape(1, start_id=100, end_id=10)

    def test_chunksize_1(self):
        """Ensure valid range between start_id and end_id values."""
        results = self.scraper.scrape(1, start_id=1, end_id=10)
        for item in results:
            assert len(item) == 1

    def test_chunksize_10(self):
        """Ensure valid range between start_id and end_id values."""
        results = self.scraper.scrape(10, start_id=1, end_id=10)
        for item in results:
            assert len(item) == 10            
        
