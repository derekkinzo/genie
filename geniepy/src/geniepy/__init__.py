"""GeniePy Package entry point."""
from pkg_resources import get_distribution, DistributionNotFound
import geniepy.config as config
from geniepy.datamgmt import DaoManager
from geniepy.classmgmt import ClassificationMgr
import geniepy.datamgmt.repositories as dr

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


__all__ = ["run", "run_predictions", "update_tables"]


def run_predictions():
    """Calculate predictions for all records in database."""
    features, scores = config.get_repos()
    classifier = config.get_classifier()
    query_all = features.query_all
    for record_df in scoring_repo.query(query_all, config.get_chunksize):
        predicted_df = classifier.predict(record_df)
        scores.save(predicted_df)

    # chunksize = config.get_chunksize()
    # for records in daomgr.gen_records(chunksize):
    #     predicted_df = classmgr.predict(records)
    #     daomgr.save_predictions(predicted_df)


def update_tables():
    """Call scrapes to download data and create/append tables."""
    daomgr: DaoManager = config.get_daomgr()
    chunksize = config.get_classmgr()
    daomgr.download(chunksize)


def run():
    """Cron-job function to scrape sources for updated data and update predictions."""
    print("Running...")
    print("Done")
