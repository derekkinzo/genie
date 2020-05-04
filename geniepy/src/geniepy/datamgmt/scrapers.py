"""Scraping module to fetch data from online sources."""
from pathlib import Path
from typing import Generator
from abc import ABC, abstractmethod
import wget
import gzip
import shutil
import os
import pandas as pd
from ftplib import FTP
import xml.etree.ElementTree as ET
from geniepy.pubmed import PubMedArticle


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
    # Class Variables
    _PUBMED_FTP_SERVER = "ftp.ncbi.nlm.nih.gov"
    _PUBMED_FTP_DIR = "/pubmed/updatefiles/"
    _PUBMED_FILE_EXT = ".xml.gz"
    _WORKING_DIR = "./"
    _DATA_FILE = "./pubmed_parsed.dat"

    old_files = []
    new_files = []

    def _ftp_connect(self):
        try:
            ftp = FTP(PubMedScraper._PUBMED_FTP_SERVER)
            ftp.login()
            ftp.cwd(PubMedScraper._PUBMED_FTP_DIR)
            return ftp
        except Exception as e:
            return None

    def _ftp_disconnect(self, ftp: FTP):
        try:
            ftp.close()
        except Exception as e:
            return

    def _get_old_filenames(self):
        try:
            with open(PubMedScraper._DATA_FILE, "r") as f:
                for line in f.readlines():
                    self.old_files.append(line.replace('\n',''))
        except Exception as e:
            self.old_files = []

    def _is_new_file(self, file_name: str):
        if not self.old_files or len(self.old_files) <= 0:
            return True
         
        for file in self.old_files:
            if str(file).lower() == file_name.lower():
                return False
        
        return True

    def _download_new_files(self):
        ftp_files = []

        # connect to FTP and retrieve list of available files
        ftp = self._ftp_connect()
        ftp.retrlines(f'LIST *{PubMedScraper._PUBMED_FILE_EXT}', ftp_files.append)

        # find the new files available
        for _ in ftp_files:
            if self._is_new_file(_.split(' ')[-1]):
                self.new_files.append(_.split(' ')[-1])

        # download new files
        for _ in self.new_files:
            try:
                ftp.retrbinary("RETR " + _, open(f"{PubMedScraper._WORKING_DIR}{_}", 'wb').write)
            except Exception as e:
                #ignore error (could be logged later)
                pass

        # close ftp connection
        self._ftp_disconnect(ftp)

    def _clean_up(self):
        # update old file names
        with open(PubMedScraper._DATA_FILE, "a+") as f:
            f.writelines(map(lambda x:x+'\n', self.new_files))

        # remove downloaded files
        for _ in self.new_files:
            os.remove(f"{PubMedScraper._WORKING_DIR}{_}")                                                        

    def scrape(self, chunksize: int, **kwargs) -> Generator:
        """
        Implement base scrape method to download records from PubMed database.

        Keyword Arguments:
            chunksize {int} -- the size of each chunk the data should be returned

        Returns:
            Generator -- The generator yielding the data in given chunksizes.
        """

        self._get_old_filenames()
        self._download_new_files()

        #uncompress each PubMed file & scrape its contents
        pubmed_articles: [PubMedArticle] = []
        for _ in self.new_files:
            with gzip.open(f"{PubMedScraper._WORKING_DIR}{_}", 'rb') as f:
                xml_root = ET.fromstring(f.read())
                xml_list = xml_root.findall("PubmedArticle")
                for article_xml in xml_list:
                    pubmed_articles.append(PubMedArticle(article_xml))

            # yield articles to generator
            while True:
                articles_chunk = []
                for _ in range(chunksize):
                    if len(pubmed_articles) > 0:
                        articles_chunk.append(pubmed_articles.pop())
                if len(articles_chunk) <= 0:
                    break

                yield articles_chunk
        
        self._clean_up()
        # raise NotImplementedError
