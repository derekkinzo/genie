"""Scraping module to fetch data from online sources."""
from typing import Generator
from abc import ABC, abstractmethod


class BaseScraper(ABC):
    """Scraper Abstract Base Class."""

    @abstractmethod
    def scrape(self, chunksize: int, **kwargs) -> Generator:
        """
        Download any new information not yet downloaded.

        The first time this method is called, it should download and return
        all available information from the online source to build the internal
        databases. Subsequent calls to the scrape function should only return
        data that is new and has not yet been downloaded.

        Since the data downloaded can be too large to be loaded into memory at
        once, it should be yielded incrementally in chunks. Refer to the chunksize
        argument to determine how much data should be yielded at a time.

        Keyword Arguments:
            chunksize {int} -- the size of each chunk the data should be returned

        Returns:
            Generator -- The generator yielding the data in given chunksizes.
        """


class CtdScraper(BaseScraper):
    """
    Implementation of CTD Gene-Disease Relationship Scraper.

    http://ctdbase.org/
    """

    def scrape(self, chunksize: int, **kwargs) -> Generator:
        """
        Implement base scrape method to download records from CTD database.

        Keyword Arguments:
            chunksize {int} -- the size of each chunk the data should be returned

        Returns:
            Generator -- The generator yielding the data in given chunksizes.
        """
        raise NotImplementedError


class PubMedScraper(BaseScraper):
    """
    Implementation of PubMed Articles Scraper.

    https://www.ncbi.nlm.nih.gov/pubmed/
    https://www.nlm.nih.gov/bsd/licensee/elements_descriptions.html

    """

    def scrape(self, chunksize: int, **kwargs) -> Generator:
        """
        Implement base scrape method to download records from PubMed database.

        Keyword Arguments:
            chunksize {int} -- the size of each chunk the data should be returned

        Returns:
            Generator -- The generator yielding the data in given chunksizes.
        """
        raise NotImplementedError
