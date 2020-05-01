"""Scraping module to fetch data from online sources."""
from typing import Generator
from abc import ABC, abstractmethod
from ftplib import FTP
import os
import gzip
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
        for _ in new_files:
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
        
        self._clean_up()

        while True:
            articles_chunk = []
            for _ in range(chunksize):
                # Append articles to create chunk sized array
                if len(xml_list) > 0:
                    articles_chunk.append(xml_list.pop())
            # If no more articles return
            if not articles_chunk:
                return
            # If still articles, yield to generator
            yield articles_chunk

        # raise NotImplementedError
        
