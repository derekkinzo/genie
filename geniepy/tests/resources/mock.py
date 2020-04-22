"""Mock framework for tests."""
import os
from typing import NamedTuple
from typing import Generator
from tests import get_resources_path
from geniepy.classifiers.clsfr_base import BaseClsfr
from geniepy.datamgmt.scrapers import BaseScraper
import xml.etree.ElementTree as ET
from geniepy import CHUNKSIZE
from geniepy.pubmed import ArticleSetParser, PubMedArticle


class MockPubMedScraper(BaseScraper):
    """Mock PubMed scraper for tests."""

    filename: str = "sample_articleset1.xml"

    def scrape(self, chunksize: int = CHUNKSIZE, **kwargs) -> Generator:
        """Simulate scraping pubmed baseline and returning xml objs."""
        xml_file_path = os.path.join(get_resources_path(), self.filename)
        xml_root: ET.Element = ET.parse(xml_file_path).getroot()

        xml_list = xml_root.findall("PubmedArticle")
        pubmed_articles: [PubMedArticle] = []
        for article_xml in xml_list:
            pubmed_articles.append(PubMedArticle(article_xml))

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


class MockCtdScraper(BaseScraper):
    """Mock CTD scraper for tests."""

    filename: str = "sample_ctd_db.csv"

    def scrape(self, chunksize: int = CHUNKSIZE, **kwargs) -> Generator:
        """Simulate scraping records and returning csv str."""
        csv_file = os.path.join(get_resources_path(), self.filename)
        # Open a connection to the file
        with open(csv_file) as file:
            # Read header
            header = file.readline()
            # Loop indefinitely until the end of the file
            while True:
                data = ""
                for _ in range(chunksize):
                    line = file.readline()
                    if not line:
                        break
                    data += line
                if not data:
                    break
                chunk = header + data
                yield chunk


class MockClsfr(BaseClsfr):
    """Implementation of Mock Classifier."""

    class Attributes(NamedTuple):
        """Attributes of mock classifier."""

        featureA: int = 1
        """Example of a integer attribute."""
        featureB: str = "default"
        """Example of a string attribute."""
        label: int = 0
        """Example of a integer label."""

    def restore_model(self) -> bool:
        """
        Load classifier model from memory.

        Returns:
            bool -- True if model loaded successfully, False otherwise.
        """
        return True

    def store_model(self) -> bool:
        """
        Store classifier model into memory.

        Returns:
            bool -- True if model saves successfully, False otherwise.
        """
        return True

    def __init__(self):
        # pylint: disable=W0235
        """
        Initialize classifier.

        Restore classifier model from memory if it exists. Otherwise, train classifier.
        """
        super().__init__()
        self.mock_prediction = 1

    def fit(self, features: [Attributes]) -> str:
        """Train classifier given dataset."""
        self.mock_prediction = 2
        self._is_trained = "String containing training stats"

    def predict(self, features: Attributes):
        """Calculate publication count label."""
        return self.mock_prediction