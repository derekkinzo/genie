"""Scraping module to fetch data from online sources."""
import binascii
from pathlib import Path
from typing import Generator
from abc import ABC, abstractmethod
import wget
import gzip
import shutil
import os
import pandas as pd
import geniepy.config as config
from ftplib import FTP
import requests
import xml.etree.ElementTree as ET
from random import randint
from pathlib import Path
from geniepy.pubmed import PubMedArticle
from joblib import Memory


# Initialize memoization
memory = Memory(str(config.TMP_DIR), verbose=0)


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

    SOURCE_NAME = "Pubtator Genes"
    TMP_DIR = config.TMP_DIR
    FTP_URL = "ftp://ftp.ncbi.nlm.nih.gov/pub/lu/PubTatorCentral/gene2pubtatorcentral.gz"  # noqa
    SAMPLE_FTP_URL = "ftp://ftp.ncbi.nlm.nih.gov/pub/lu/PubTatorCentral/gene2pubtatorcentral.sample"  # noqa
    DOWNLOAD_NAME = "pubtator-gene.download"
    CSV_NAME = "pubtator-gene.csv"
    HEADER_NAMES = ["PMID", "Type", "GeneID", "Mentions", "Resource"]

    def __init__(self):
        self.TMP_DIR.mkdir(parents=True, exist_ok=True)

    @property
    def download_path(self):
        """Path to pubtator gzip downloaded file."""
        download_path = self.TMP_DIR.joinpath(self.DOWNLOAD_NAME).resolve()
        return download_path

    @property
    def csv_path(self):
        """Path to pubtator csv downloaded file."""
        csv_path = self.TMP_DIR.joinpath(self.CSV_NAME).resolve()
        return csv_path

    def is_gzip(self, filepath) -> bool:
        """Check if file is gzipped."""
        with open(filepath, "rb") as test_f:
            return binascii.hexlify(test_f.read(2)) == b"1f8b"

    def download(self):
        """Download records from online sources."""
        print(f"Downloading {self.SOURCE_NAME} records...")
        if not self.download_path.exists():
            wget.download(self.FTP_URL, str(self.download_path))
        if self.is_gzip(self.download_path):
            with gzip.open(self.download_path, "rb") as f_in:
                with open(self.csv_path, "wb") as f_out:
                    shutil.copyfileobj(f_in, f_out)
        else:
            self.download_path.rename(self.csv_path)
        self.clean_up()

    def set_sample(self, kwargs):
        """Set sample url if is_sample is set."""
        if kwargs.get("is_sample"):
            self.FTP_URL = self.SAMPLE_FTP_URL

    def scrape(self, chunksize: int, **kwargs) -> Generator:
        """
        Download pmid/geneid data from pubtator.

        ftp://ftp.ncbi.nlm.nih.gov/pub/lu/PubTatorCentral/disease2pubtatorcentral.gz
        """
        self.set_sample(kwargs)
        if kwargs.get("baseline"):
            self.download()
            csv_gen = pd.read_csv(
                self.csv_path,
                chunksize=chunksize,
                delimiter="\t",
                names=self.HEADER_NAMES,
            )
            return csv_gen
        return ()

    def clean_up(self):
        """Delete all temp files."""
        if os.path.exists(self.download_path):
            os.remove(self.download_path)


class PubtatorDiseaseScraper(PubtatorGeneScraper):
    """Scrape PMID/DiseaseID from pubtator."""

    SOURCE_NAME = "Pubtator Diseases"
    FTP_URL = "ftp://ftp.ncbi.nlm.nih.gov/pub/lu/PubTatorCentral/disease2pubtatorcentral.gz"  # noqa
    SAMPLE_FTP_URL = "ftp://ftp.ncbi.nlm.nih.gov/pub/lu/PubTatorCentral/disease2pubtatorcentral.sample"  # noqa
    DOWNLOAD_NAME = "pubtator-disease.download"
    CSV_NAME = "pubtator-disease.csv"
    HEADER_NAMES = ["PMID", "Type", "DiseaseID", "Mentions", "Resource"]


class SjrScraper(PubtatorGeneScraper):
    """Scrape Scientific Journal Ratings records."""

    SOURCE_NAME = "SJR"
    FTP_URL = "https://www.scimagojr.com/journalrank.php?out=xls"  # noqa
    SAMPLE_FTP_URL = "https://www.scimagojr.com/journalrank.php?area=1100&out=xls"
    CSV_NAME = "sjr.csv"

    def scrape(self, chunksize: int, **kwargs) -> Generator:
        """Download sjr data."""
        self.set_sample(kwargs)
        if kwargs.get("baseline") is True:
            # Only download if baseline is true
            self.download()
            csv_gen = pd.read_csv(self.csv_path, chunksize=chunksize, delimiter=";")
            return csv_gen
        return ()


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

    # Logger
    LOGGER = config.get_logger("PubMedScraper")

    # Constants for PubMed scraping
    DEFAULT_CHUNKSIZE: int = 1000
    DEFAULT_PUBMED_BASELINE_SCRAPE_MODE: bool = False
    DEFAULT_PUBMED_FTP_SERVER: str = "ftp.ncbi.nlm.nih.gov"
    DEFAULT_PUBMED_BASELINE_DIR: str = "/pubmed/baseline/"
    DEFAULT_PUBMED_UPDATE_DIR: str = "/pubmed/updatefiles/"
    DEFAULT_PUBMED_DATA_FILE = "~/.geniepy.d/pubmed.dat"
    DEFAULT_DOWNLOAD_DIR = "~/.geniepy.d/tmp/"
    DEFAULT_PUBMED_DATAFILE_EXTN = ".xml.gz"
    DEFAULT_DOWNLOAD_RETRIES = 2

    # Constants for PubMed scraping
    TAG_ARTICLE = "PubmedArticle"

    # Constants for Citation scraping
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

    def __init__(self):
        """Initialize memoization for citation scraping."""
        self._citationScrape = memory.cache(self._citationScrape)

    def scrape(self, chunksize: int, **kwargs) -> Generator:
        """
        Implement base scrape method to download records from PubMed database.

        Keyword Arguments:
            chunksize {int} -- the size of each chunk the data should be returned

        Returns:
            Generator -- The generator yielding the data in given chunksizes.
        """
        PubMedScraper.LOGGER.info("Starting PubMed Scraper")

        # set default chunksize
        if chunksize <= 0:
            chunksize = PubMedScraper.DEFAULT_CHUNKSIZE
            PubMedScraper.LOGGER.info(f"chunksize set to default: {chunksize}")

        # set IS_SAMPLE flag
        IS_SAMPLE = False
        if "is_sample" in kwargs:
            try:
                IS_SAMPLE = kwargs.get("is_sample")
            except:
                IS_SAMPLE = False

        # set BASELINE_SCRAPE_MODE flag
        # BASELINE_SCRAPE_MODE = True (enables the baseline scraping mode)
        # BASELINE_SCRAPE_MODE = Flase (enables the update scraping mode)
        BASELINE_SCRAPE_MODE: bool = PubMedScraper.DEFAULT_PUBMED_BASELINE_SCRAPE_MODE
        if "baseline" in kwargs:
            try:
                if kwargs.get("baseline") == True:
                    BASELINE_SCRAPE_MODE = True
                    PubMedScraper.LOGGER.info("Scrape mode: Baseline")
            except Exception as e:
                BASELINE_SCRAPE_MODE = PubMedScraper.DEFAULT_PUBMED_BASELINE_SCRAPE_MODE
                PubMedScraper.LOGGER.exception(e.msg())
                PubMedScraper.LOGGER.info("Scrape mode: Daily Update")
        else:
            PubMedScraper.LOGGER.info("Scrape mode: Daily Update")

        # set PubMed FTP server
        FTP_SERVER: str = ""
        try:
            FTP_SERVER = config.get_pubmed_ftp_server()
        except Exception as e:
            FTP_SERVER = PubMedScraper.DEFAULT_PUBMED_FTP_SERVER
            PubMedScraper.LOGGER.exception(e.msg())

        PubMedScraper.LOGGER.info(f"FTP_SERVER: {FTP_SERVER}")

        # set PubMed FTP directory
        FTP_DIR: str = ""
        if BASELINE_SCRAPE_MODE:
            # we are in baseline scrape mode. get baseline dataset directory
            try:
                FTP_DIR = config.get_pubmed_baseline_dir()
            except Exception as e:
                FTP_DIR = PubMedScraper.DEFAULT_PUBMED_BASELINE_DIR
                PubMedScraper.LOGGER.exception(e.msg())
        else:
            # we are in update scrape mode. get baseline dataset directory
            try:
                FTP_DIR = config.get_pubmed_update_dir()
            except Exception as e:
                FTP_DIR = PubMedScraper.DEFAULT_PUBMED_UPDATE_DIR
                PubMedScraper.LOGGER.exception(e.msg())

        PubMedScraper.LOGGER.info(f"FTP_DIR: {FTP_DIR}")

        # connect to pubmed ftp and retrieve list of ftp files
        pubmed_ftp = self._ftp_connect(FTP_SERVER, FTP_DIR)
        pubmed_files = self._ftp_file_list(pubmed_ftp)  # list of files from ftp
        pubmed_history = self._read_history()  # list of historically scraped files

        PubMedScraper.LOGGER.info(f"Number of files in FTP: {len(pubmed_files)}")
        PubMedScraper.LOGGER.info(f"Number of files in History: {len(pubmed_history)}")

        # determine new files to parse
        # in BASELINE_SCRAPE_MODE parse all files
        pubmed_new_files = []
        parsed_files = []
        if BASELINE_SCRAPE_MODE:
            pubmed_new_files = pubmed_files
        else:
            pubmed_new_files = list(set(pubmed_files) - set(pubmed_history))

        PubMedScraper.LOGGER.info(
            f"Number of new files to be parsed: {len(pubmed_new_files)}"
        )

        # main scraping block
        try:
            for pubmed_file in pubmed_new_files:
                # download pubmed data file
                retries = 0
                while retries <= PubMedScraper.DEFAULT_DOWNLOAD_RETRIES:
                    if self._ftp_download(pubmed_ftp, pubmed_file):
                        PubMedScraper.LOGGER.info(
                            f"Downloaded PubMed file: {pubmed_file}"
                        )
                        break
                    retries += 1

                # scrape downloaded PubMed data file
                articles = self._pubmedScrape(pubmed_file)
                PubMedScraper.LOGGER.info(
                    f"{len(articles)} articles found in {pubmed_file}"
                )

                # optimize chunksize based on number of
                # available PubMed articles
                chunk_size: int = 0
                if chunksize > len(articles):
                    chunk_size = len(articles)
                else:
                    chunk_size = chunksize
                PubMedScraper.LOGGER.info(f"Chunksize is set to: {chunk_size}")

                # yield articles to generator
                while True:
                    articles_chunk = []
                    for i in range(chunk_size):
                        if len(articles) > 0:
                            article = articles.pop()
                            if not IS_SAMPLE or (IS_SAMPLE and i <= 1000):
                                # scrape citation metadata
                                # in is_sample mode only scrape first 1000 citations
                                citations = self._citationScrape(article.pmid)
                                article.set_citationCount(citations[1])
                                article.set_citationPmid(citations[2])
                                PubMedScraper.LOGGER.info(
                                    f"Get citations for PMID: {article.pmid} [{i} of {chunk_size}]"
                                )
                            articles_chunk.append(article)
                        else:
                            break

                    if len(articles_chunk) <= 0:
                        break

                    PubMedScraper.LOGGER.info(f"Yielded {len(articles_chunk)} articles")
                    yield articles_chunk

                # update list of parsed files
                parsed_files.append(pubmed_file)

        except GeneratorExit:
            # ignore error.
            pass

        finally:
            # close ftp connection
            self._ftp_disconnect(pubmed_ftp)
            PubMedScraper.LOGGER.info("FTP disconnected")

            # clean up downloaded files
            self._clean_up()
            PubMedScraper.LOGGER.info("PubMed Scraper: Clean-up")

            # update history
            self._update_history(parsed_files)
            PubMedScraper.LOGGER.info("PubMed Scraper: Updated History")

            # if baseline dataset was scraped; reset scrape history
            if BASELINE_SCRAPE_MODE:
                self._clear_history()
                PubMedScraper.LOGGER.info(
                    "PubMed Scraper: Cleared History (after BASELINE)"
                )

        return

    def _ftp_connect(self, ftp_server, ftp_dir) -> FTP:
        """Opens FTP connection and returns the FTP handle"""
        try:
            ftp = FTP(ftp_server)
            ftp.login()
            ftp.cwd(ftp_dir)
            return ftp
        except Exception as e:
            PubMedScraper.LOGGER.exception(e.msg())
            return None

    def _ftp_disconnect(self, ftp: FTP):
        """Disconnect and close FTP connection"""
        try:
            ftp.close()
            return
        except Exception as e:
            PubMedScraper.LOGGER.exception(e.msg())
            return

    def _ftp_file_list(self, ftp: FTP) -> []:
        """Read list of files in FTP directory"""
        ftp_files = []
        try:
            ftp.retrlines(
                f"LIST *{PubMedScraper.DEFAULT_PUBMED_DATAFILE_EXTN}", ftp_files.append
            )
            ftp_files = [
                file.split(" ")[-1].lower() for file in ftp_files
            ]  # transform filenames
            return ftp_files
        except Exception as e:
            PubMedScraper.LOGGER.exception(e.msg())
            return ftp_files

    def _ftp_download(self, ftp: FTP, ftp_file: str) -> bool:
        """Downloads given file from the FTP server"""
        try:
            # check if the download path exists.
            # if not, create the path
            download_path = os.path.expanduser(self._get_download_dir())
            Path(download_path).mkdir(parents=True, exist_ok=True)

            # downlad file
            download_filepath = os.path.join(download_path, ftp_file)
            ftp.retrbinary("RETR " + ftp_file, open(download_filepath, "wb").write)
            return True
        except Exception as e:
            PubMedScraper.LOGGER.exception(e.msg())
            return False

    def _read_history(self) -> []:
        """Read and create list of PubMed filenames
        which are already scraped"""
        history = []
        try:
            with open(self._get_history_filepath(), "r") as f:
                for line in f.readlines():
                    history.append(line.replace("\n", "").lower())
            return history
        except Exception as e:
            PubMedScraper.LOGGER.info(
                "History file not found. New History file will be created."
            )
            return []

    def _update_history(self, file_list: []):
        """Read and create list of PubMed filenames
        which are already scraped"""
        try:
            with open(self._get_history_filepath(), "a+") as f:
                f.writelines(map(lambda x: x + "\n", file_list))
        except Exception as e:
            PubMedScraper.LOGGER.exception(e.msg())
            return

    def _clear_history(self):
        """Clear scrape history"""
        history_file = self._get_history_filepath()
        if os.path.exists(history_file):
            os.remove(history_file)
        pass

    def _get_history_filepath(self) -> str:
        """Get PubMed data file path from Config"""
        try:
            history_file_path = os.path.expanduser(config.get_pubmed_data_file())
            return history_file_path
        except Exception as e:
            PubMedScraper.LOGGER.exception(e.msg())
            return PubMedScraper.DEFAULT_PUBMED_BASELINE_DIR

    def _get_download_dir(self) -> str:
        """Get path where to download PubMed data files"""
        try:
            return config.get_pubmed_download_dir()
        except Exception as e:
            PubMedScraper.LOGGER.exception(e.msg())
            return PubMedScraper.DEFAULT_DOWNLOAD_DIR

    def _pubmedScrape(self, pubmed_file) -> []:
        """Scrape all pubmed articles from pubmed data file"""
        pubmed_articles = []
        try:
            file_path = os.path.expanduser(self._get_download_dir())
            file = os.path.join(file_path, pubmed_file)
            with gzip.open(file, "rb") as f:
                xml_root = ET.fromstring(f.read())
                xml_list = xml_root.findall(PubMedScraper.TAG_ARTICLE)
                for article_xml in xml_list:
                    pubmed_articles.append(PubMedArticle(article_xml))
            return pubmed_articles
        except Exception as e:
            PubMedScraper.LOGGER.exception(e.msg())
            return []

    def _citationScrape(self, pmid: int) -> []:
        """Scrape citation metadata from PubMed API"""
        null_citation = [pmid, 0, ""]

        # fire PubMed API request
        try:
            req = requests.get(PubMedScraper._citationApiUrl(pmid))
            tree = ET.fromstring(req.text)
        except Exception as e:
            PubMedScraper.LOGGER.exception(e.msg())
            return null_citation

        # scrape citation data from API response
        citation_tree = tree.findall(PubMedScraper.TAG_CITATION_ID)
        if citation_tree and len(citation_tree) > 0:
            citations = []
            for _ in citation_tree:
                citations.append(_.text)
            return [pmid, len(citation_tree), ",".join(citations)]

        return null_citation

    def _clean_up(self):
        """Delete all downloaded pubmed files"""
        clean_up_path = os.path.expanduser(self._get_download_dir())
        try:
            shutil.rmtree(clean_up_path)
            return
        except OSError as e:
            PubMedScraper.LOGGER.exception(e.msg())
            return

    @classmethod
    def _citationApiUrl(cls, pmid: int) -> str:
        """Returns a fully formated citation API URL for a given PMID"""
        return (
            PubMedScraper.API_BASE_URL
            + PubMedScraper.API_KEY_PARAM
            + PubMedScraper._randomApiKey()
            + PubMedScraper.API_ID_PARAM
            + str(pmid)
        )

    @classmethod
    def _randomApiKey(cls) -> str:
        """Returns a random PubMed API key from a list of static API keys"""
        return PubMedScraper.API_KEYS[randint(0, len(PubMedScraper.API_KEYS) - 1)]
