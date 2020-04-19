"""Mock framework for tests."""
import os
from typing import NamedTuple
from typing import Generator
from tests import get_resources_path
from geniepy.classifiers.clsfr_base import BaseClsfr
from geniepy.datamgmt.scrapers import CtdScraper
from geniepy import CHUNKSIZE


SAMPLE_CTD_DB_NAME = "sample_ctd_db.csv"


class MockCtdScraper(CtdScraper):
    """Mock CTD scraper for tests."""

    @staticmethod
    def scrape(chunksize: int = CHUNKSIZE) -> Generator:
        """Scrape records from online source and return in generator."""
        sample_ctd_name = "sample_ctd_db.csv"
        csv_file = os.path.join(get_resources_path(), sample_ctd_name)
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
