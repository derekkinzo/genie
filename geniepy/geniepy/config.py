"""
GeniePy Configuration Module.

This module is intended to provide functions that interprets content from the
package configuration file and generate the corresponding python objects.
"""
import geniepy.datamgmt.daos as daos
import geniepy.datamgmt.repositories as dr
from geniepy.datamgmt.tables import PUBMED_PROPTY, CTD_PROPTY, CLSFR_PROPTY
from geniepy.datamgmt import DaoManager
from geniepy.classmgmt import ClassificationMgr

# TODO remove mock
import tests.resources.mock as mock
from tests import get_test_output_path
import os


# TODO Retrieve from config file
def get_chunksize():
    """Retrieve standard genie generators chunk size."""
    chunksize: int = 10 ** 4
    return chunksize


def get_daomgr() -> DaoManager:
    # TODO Retrieve from config file
    """Configure data mgmt subsystem."""
    credentials_file = "genie_credentials.json"
    credentials_path = os.path.join(get_test_output_path(), credentials_file)
    # Google BigQuery Project Name
    project_name = "genie-275215"
    gbq_dataset = "test"

    ctd_dao = daos.CtdDao(
        dr.GbqRepository(project_name, CTD_PROPTY, gbq_dataset, credentials_path)
    )
    # pylint: disable=protected-access
    ctd_dao._parser.scraper = mock.MockCtdScraper()

    # Create and configure mock pubmed dao
    pubmed_dao = daos.PubMedDao(
        dr.GbqRepository(project_name, PUBMED_PROPTY, gbq_dataset, credentials_path)
    )
    # pylint: disable=protected-access
    pubmed_dao._parser.scraper = mock.MockPubMedScraper()

    # Create and configure mock classifier dao
    classifier_dao = daos.ClassifierDao(
        dr.GbqRepository(project_name, CLSFR_PROPTY, gbq_dataset, credentials_path)
    )

    # Construct mock dao manager for testing
    daomgr = DaoManager(
        ctd_dao=ctd_dao, pubmed_dao=pubmed_dao, classifier_dao=classifier_dao
    )
    return daomgr


def get_classmgr() -> ClassificationMgr:
    # TODO Retrieve from config file
    """Configure classification mgmt subsystem."""
    return mock.MOCK_CLSFRMGR
