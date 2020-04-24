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


def run_job():
    """Cron-job function to scrape sources for updated data and update predictions."""
    raise NotImplementedError
