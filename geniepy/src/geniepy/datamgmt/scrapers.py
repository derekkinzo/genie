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
    def gzip_path(self):
        """Path to pubtator gzip downloaded file."""
        gzip_path = self.TMP_DIR.joinpath(self.GZIP_NAME).resolve()
        return gzip_path

    @property
    def csv_path(self):
        """Path to pubtator csv downloaded file."""
        csv_path = self.TMP_DIR.joinpath(self.CSV_NAME).resolve()
        return csv_path

    def download(self):
        """Download records from online sources."""
        if not self.gzip_path.exists():
            wget.download(self.FTP_URL, str(self.gzip_path))
            with gzip.open(self.gzip_path, "rb") as f_in:
                with open(self.csv_path, "wb") as f_out:
                    shutil.copyfileobj(f_in, f_out)

    def scrape(self, chunksize: int, **kwargs) -> Generator:
        """
        Download pmid/geneid data from pubtator.

        ftp://ftp.ncbi.nlm.nih.gov/pub/lu/PubTatorCentral/disease2pubtatorcentral.gz
        """
        self.download()
        csv_gen = pd.read_csv(
            self.csv_path, chunksize=chunksize, delimiter="\t", names=self.HEADER_NAMES,
        )
        return csv_gen

    def clean_up(self):
        """Delete all temp files."""
        if os.path.exists(self.gzip_path):
            os.remove(self.gzip_path)
        if os.path.exists(self.csv_path):
            os.remove(self.csv_path)


class PubtatorDiseaseScraper(PubtatorGeneScraper):
    """Scrape PMID/DiseaseID from pubtator."""

    FTP_URL = "ftp://ftp.ncbi.nlm.nih.gov/pub/lu/PubTatorCentral/disease2pubtatorcentral.gz"  # noqa
    GZIP_NAME = "pubtator-disease.gzip"
    CSV_NAME = "pubtator-disease.csv"
    HEADER_NAMES = ["PMID", "Type", "DiseaseID", "Mentions", "Resource"]


class SjrScraper(BaseScraper):
    """Scrape Scientific Journal Ratings records."""

    TMP_DIR = Path.cwd().joinpath("tmp")
    FTP_URL = "https://www.scimagojr.com/journalrank.php?out=xls"  # noqa
    CSV_NAME = "sjr.csv"

    def __init__(self):
        self.TMP_DIR.mkdir(parents=True, exist_ok=True)

    @property
    def csv_path(self):
        """Path to pubtator csv downloaded file."""
        csv_path = self.TMP_DIR.joinpath(self.CSV_NAME).resolve()
        return csv_path

    def download(self):
        """Download records from online sources."""
        if not self.csv_path.exists():
            wget.download(self.FTP_URL, str(self.csv_path))

    def scrape(self, chunksize: int, **kwargs) -> Generator:
        """Download sjr data."""
        self.download()
        csv_gen = pd.read_csv(self.csv_path, chunksize=chunksize, delimiter=";")
        return csv_gen

    def clean_up(self):
        """Delete all temp files."""
        if os.path.exists(self.csv_path):
            os.remove(self.csv_path)


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
