"""GeniePy Package entry point."""
from pkg_resources import get_distribution, DistributionNotFound

try:
    # Change here if project is renamed and does not equal the package name
    DIST_NAME = __name__
    __version__ = get_distribution(DIST_NAME).version
except DistributionNotFound:
    __version__ = "unknown"
finally:
    del get_distribution, DistributionNotFound

__author__ = "The Harvard LAMP Team"
__copyright__ = "The Harvard LAMP Team"
__license__ = "MIT"


__all__ = ["run_job"]


CHUNKSIZE: int = 10 ** 4
"""Standard genie generators chunk size."""


def update_tables():
    """Scrape internet for new content from sources and update database."""
    raise NotImplementedError


def update_predictions():
    """Iterate over tables and calculate needed classifier scores."""
    # trials_classifier = ClassifierClinicalTrials()
    # run classifier on gene-disease relationship
    # pcp_data_set = None
    # pcp_classifier = ClassifierPCP()
    # publication_prediction = pcp_classifier.predict(pcp_data_set)
    raise NotImplementedError


def run_job():
    """Cron-job function to scrape sources for updated data and update predictions."""
    # Make sure tables are up-to-date with available online content
    update_tables()
    # Update table with classifier scores
    update_predictions()
    raise NotImplementedError
