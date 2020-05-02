"""Scraping module to fetch data from online sources."""
from pathlib import Path
from typing import Generator
from abc import ABC, abstractmethod
import wget
import gzip
import shutil
import os
import pandas as pd


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


class PubtatorGeneScraper(BaseScraper):
    """Scrape PMID/GENEID from pubtator."""

    TMP_DIR = Path.cwd().joinpath("tmp")
    FTP_URL = "ftp://ftp.ncbi.nlm.nih.gov/pub/lu/PubTatorCentral/gene2pubtatorcentral.gz"  # noqa
    PUBTATOR_GZIP_NAME = TMP_DIR.joinpath("pubtator-gene.gzip").resolve()
    PUBTATOR_CSV_NAME = TMP_DIR.joinpath("pubtator-gene.csv").resolve()

    def __init__(self):
        self.TMP_DIR.mkdir(parents=True, exist_ok=True)

    def download(self):
        """Download records from online sources."""
        wget.download(self.FTP_URL, str(self.PUBTATOR_GZIP_NAME))
        with gzip.open(self.PUBTATOR_GZIP_NAME, "rb") as f_in:
            with open(self.PUBTATOR_CSV_NAME, "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)

    def scrape(self, chunksize: int, **kwargs) -> Generator:
        """
        Download pmid/geneid data from pubtator.

        ftp://ftp.ncbi.nlm.nih.gov/pub/lu/PubTatorCentral/gene2pubtatorcentral.gz
        """

        header_names = ["PMID", "Type", "Concept ID", "Mentions", "Resource"]
        csv_gen = pd.read_csv(
            self.PUBTATOR_CSV_NAME,
            chunksize=chunksize,
            delimiter="\t",
            names=header_names,
        )
        return csv_gen

    def clean_up(self):
        """Delete all temp files."""
        if os.path.exists(self.PUBTATOR_GZIP_NAME):
            os.remove(self.PUBTATOR_GZIP_NAME)
        if os.path.exists(self.PUBTATOR_CSV_NAME):
            os.remove(self.PUBTATOR_CSV_NAME)


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
