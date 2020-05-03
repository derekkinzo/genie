"""Mock framework for tests."""
import os
from typing import Generator
import xml.etree.ElementTree as ET
import pandas as pd
from tests import get_resources_path
from geniepy.datamgmt.scrapers import BaseScraper, PubtatorGeneScraper
from geniepy.pubmed import PubMedArticle
from geniepy.classmgmt import ClassificationMgr
from geniepy.classmgmt.classifiers import Classifier

TEST_CHUNKSIZE = 5
"""Default chunksize for tests."""


class MockClassifier(Classifier):
    """Mock classifier for tests."""

    def load(self):
        """
        Load classifier model.
        Raises:
            ClassifierError -- If model doesn't load successfully
        """
        self._model = True
        self._is_trained = True


PCPCLSFR = MockClassifier("pub_score")
CTCLSFR = MockClassifier("ct_score")
# pylint: disable=protected-access
CTCLSFR._col_name = "ct_score"
MOCK_CLSFRMGR: ClassificationMgr = ClassificationMgr([PCPCLSFR, CTCLSFR])


class MockPubtatorGeneScraper(PubtatorGeneScraper):
    def scrape(self, chunksize: int, **kwargs) -> Generator:
        """Mock scrape method."""
        header_names = ["PMID", "Type", "GeneID", "Mentions", "Resource"]
        vals = [[10001], ["Gene"], [112331], ["Mention"], ["Resources"]]
        zipped = list(zip(header_names, vals))
        yield pd.DataFrame(dict(zipped))


class MockPubMedScraper(BaseScraper):
    """Mock PubMed scraper for tests."""

    filename: str = "sample_articleset2.xml"

    def scrape(self, chunksize: int = 2, **kwargs) -> Generator:
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

    def scrape(self, chunksize: int, **kwargs) -> Generator:
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
