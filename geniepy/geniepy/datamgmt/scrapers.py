"""Scraping module to fetch data from online sources."""
from typing import Generator
from abc import ABC, abstractmethod
from geniepy import CHUNKSIZE


class BaseScraper(ABC):
    """Scraper Abstract Base Class."""

    @abstractmethod
    def scrape(self, chunksize: int = CHUNKSIZE, **kwargs) -> Generator:
        """Scrape data from online source."""


class CtdScraper(BaseScraper):
    """
    Implementation of CTD Gene-Disease Relationship Scraper.

    http://ctdbase.org/
    """

    def scrape(self, chunksize: int = CHUNKSIZE, **kwargs) -> Generator:
        """Scrape records from online source and return in generator."""
        raise NotImplementedError


class PubMedScraper(BaseScraper):
    """
    Implementation of PubMed Articles Scraper.

    https://www.ncbi.nlm.nih.gov/pubmed/
    https://www.nlm.nih.gov/bsd/licensee/elements_descriptions.html

    """

    def scrape(self, chunksize: int = CHUNKSIZE, **kwargs) -> Generator:
        """Scrape records from online source and return in generator."""
        raise NotImplementedError