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
    GZIP_NAME = "pubtator-gene.gzip"
    CSV_NAME = "pubtator-gene.csv"
    HEADER_NAMES = ["PMID", "Type", "GeneID", "Mentions", "Resource"]

    def __init__(self):
        self.TMP_DIR.mkdir(parents=True, exist_ok=True)

    @property
    def pubtator_gzip(self):
        """Path to pubtator gzip downloaded file."""
        pubtator_gzip = self.TMP_DIR.joinpath(self.GZIP_NAME).resolve()
        return pubtator_gzip

    @property
    def pubtator_csv(self):
        """Path to pubtator csv downloaded file."""
        pubtator_csv = self.TMP_DIR.joinpath(self.CSV_NAME).resolve()
        return pubtator_csv

    def download(self):
        """Download records from online sources."""
        if not self.pubtator_gzip.exists():
            wget.download(self.FTP_URL, str(self.pubtator_gzip))
        if not self.pubtator_csv.exists():
            with gzip.open(self.pubtator_gzip, "rb") as f_in:
                with open(self.pubtator_csv, "wb") as f_out:
                    shutil.copyfileobj(f_in, f_out)

    def scrape(self, chunksize: int, **kwargs) -> Generator:
        """
        Download pmid/geneid data from pubtator.

        ftp://ftp.ncbi.nlm.nih.gov/pub/lu/PubTatorCentral/disease2pubtatorcentral.gz
        """
        self.download()
        csv_gen = pd.read_csv(
            self.pubtator_csv,
            chunksize=chunksize,
            delimiter="\t",
            names=self.HEADER_NAMES,
        )
        return csv_gen

    def clean_up(self):
        """Delete all temp files."""
        if os.path.exists(self.pubtator_gzip):
            os.remove(self.pubtator_gzip)
        if os.path.exists(self.pubtator_csv):
            os.remove(self.pubtator_csv)


class PubtatorDiseaseScraper(PubtatorGeneScraper):
    """Scrape PMID/DiseaseID from pubtator."""

    FTP_URL = "ftp://ftp.ncbi.nlm.nih.gov/pub/lu/PubTatorCentral/disease2pubtatorcentral.gz"  # noqa
    GZIP_NAME = "pubtator-disease.gzip"
    CSV_NAME = "pubtator-disease.csv"
    HEADER_NAMES = ["PMID", "Type", "DiseaseID", "Mentions", "Resource"]

    def download(self):
        """Download records from online sources."""
        if not self.pubtator_gzip.exists():
            wget.download(self.FTP_URL, str(self.pubtator_gzip))
            with gzip.open(self.pubtator_gzip, "rb") as f_in:
                with open(self.pubtator_csv, "wb") as f_out:
                    shutil.copyfileobj(f_in, f_out)


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
