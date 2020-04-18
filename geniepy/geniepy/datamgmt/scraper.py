"""Scraping module to fetch data from online sources."""
from typing import Generator
from abc import ABC, abstractstaticmethod
from geniepy import CHUNKSIZE


class BaseScraper(ABC):
    """Scraper Abstract Base Class."""

    @abstractstaticmethod
    def scrape(chunksize: int = CHUNKSIZE) -> Generator:
        """Scrape data from online source."""


class CtdScraper(BaseScraper):
    """
    CTD Gene-Disease Relationship Scraper.

    http://ctdbase.org/
    """

    @staticmethod
    def scrape(chunksize: int = CHUNKSIZE) -> Generator:
        """Scrape records from online source and return in generator."""
        raise NotImplementedError
