"""GeniePy Package entry point."""
from pkg_resources import get_distribution, DistributionNotFound
import geniepy.config as config
from geniepy.datamgmt import DaoManager
from geniepy.classmgmt import ClassificationMgr


# import geniepy.config as config
# from geniepy.datamgmt import DaoManager
# from geniepy.classmgmt import ClassificationMgr

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


__all__ = ["runjob"]

DAOMGR: DaoManager = config.get_daomgr()
CLASSMGR: ClassificationMgr = config.get_classmgr()
CHUNKSIZE = config.get_chunksize()


def run_predictions():
    """Calculate predictions for all records in database."""
    for records in DAOMGR.gen_records(CHUNKSIZE):
        predicted_df = CLASSMGR.predict(records)
        DAOMGR.save_predictions(predicted_df)


def run_downloads():
    """Call scrapes to download data and create/append tables."""
    DAOMGR.download(CHUNKSIZE)


def run_job():
    """Cron-job function to scrape sources for updated data and update predictions."""
    # Download all new data
    run_downloads()
    # Start parsing table
    run_predictions()
    print("Done")
