"""Scraping module to fetch data from online sources."""
from pathlib import Path
from typing import Generator
from abc import ABC, abstractmethod
import wget
import gzip
import shutil
import os
import pandas as pd
import requests
import xml.etree.ElementTree as ET
from random import randint


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


class CitationScraper(BaseScraper):
    """
    Implementation of PubMed Articles Scraper.

    https://www.ncbi.nlm.nih.gov/pubmed/
    https://www.nlm.nih.gov/bsd/licensee/elements_descriptions.html

    """

    # Constants
    API_BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?dbfrom=pubmed&linkname=pubmed_pubmed_citedin"  # noqa
    API_ID_PARAM = "&id="
    API_KEY_PARAM = "&api_key="
    API_KEYS = [
        "70b53d4e84436970587aef3493a723cae708",
        "9ab4b04dcabcab740d1a297e6f3f54aa1e09",
        "39458b83e654b32523475ee6b828b6c22c08",
        "cf95d471b41c4ea9e6b89d41de269705eb08",
        "94c3049a7b3dffca2d22ce11b51a3ea5da09",
        "3fb37654e8f711f8751d9e3c21fc46257108",
        "91315e4e69c1b5e2676371490cfc715caa08",
        "b1ee76fae01c312e4bf2fd3e8b1bcf978a09",
        "25b74bb456d7e6fc756c86c7aebb1b525009",
        "7a7e4492084dd09cef758ee65a7909704b08",
        "4d32405f13fed69766ad639d89c5c5288608",
        "18c8d26e60b5cd012e2ba9618c88dd12cb09",
        "667ca5b1b72b7697ed43c26727329282bb08",
        "5cdea4b682e2fc93c56c2b1e5e9da93f4709",
        "108b2e1a81369991da6c737545097c581a08",
        "f10805158a7609bb115cb074b05e5923a407",
        "00d74dd1cb732cd7fc29f54168fe7055c809",
    ]
    TAG_CITATION_ID = "./LinkSet/LinkSetDb/Link/Id"

    def scrape(self, chunksize: int, **kwargs) -> Generator:
        """
        Implement base scrape method to download records from PubMed database.

        Keyword Arguments:
            chunksize {int} -- the size of each chunk the data should be returned

        Returns:
            Generator -- The generator yielding the data in given chunksizes.
        """

        chunksize_min: int = 1
        chunksize_max: int = 100

        start_id: int = 1
        end_id: int = 100

        # check chunksize argument has valid value
        if chunksize < chunksize_min:
            raise ValueError(
                f"Parameter chunksize value should be between {str(chunksize_min)} and {str(chunksize_max)}"
            )

        # check start_id argument has valid value
        if "start_id" in kwargs:
            try:
                start_id = int(kwargs.get("start_id"))
            except ValueError:
                raise ValueError(
                    "Parameter start_id should be a valid numeric value greater than 0."
                )

        # check end_id argument has valid value
        if "end_id" in kwargs:
            try:
                end_id = int(kwargs.get("end_id"))
            except ValueError:
                raise ValueError(
                    "Parameter end_id should be a valid numeric value greater than 0."
                )

        # check range between start_id and end_id is valid
        if start_id >= end_id:
            raise ValueError(
                "Parameter end_id value should be greater than start_id value."
            )

        # scrape and yield Citation data
        chunk = []
        for _ in range(start_id, end_id + 1):
            if chunk and len(chunk) >= chunksize:
                yield chunk
                chunk = []

            chunk.append(self.get_citations(_))
        return

    def get_citations(self, pmid: int) -> []:
        # fire API request
        requestUrl = self.requestUrl(pmid)
        try:
            req = requests.get(requestUrl)
            tree = ET.fromstring(req.text)
        except Exception:
            # ignore error
            pass

        # scrape citation data from API response
        citation_tree = tree.findall(self.TAG_CITATION_ID)
        if citation_tree and len(citation_tree) > 0:
            citations = []
            for _ in citation_tree:
                citations.append(_.text)
            return [pmid, len(citation_tree), ",".join(citations)]

        return [pmid, 0, ""]

    def requestUrl(self, pmid: int) -> str:
        return (
            self.API_BASE_URL
            + self.API_KEY_PARAM
            + self.randomKey()
            + self.API_ID_PARAM
            + str(pmid)
        )

    def randomKey(self) -> str:
        return self.API_KEYS[randint(0, len(self.API_KEYS) - 1)]


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
