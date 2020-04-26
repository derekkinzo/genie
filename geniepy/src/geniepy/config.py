"""
GeniePy Configuration Module.

This module is intended to provide functions that interprets content from the
package configuration file and generate the corresponding python objects.
"""
import yaml
from pathlib import Path
from geniepy.errors import ConfigError
import geniepy.datamgmt.daos as daos
import geniepy.datamgmt.repositories as dr
from geniepy.datamgmt.tables import PUBMED_PROPTY, CTD_PROPTY, CLSFR_PROPTY
from geniepy.datamgmt import DaoManager
from geniepy.classmgmt import ClassificationMgr

CONFIG_NAME = "config.yaml"
CONFIG_PATH = Path(__file__).parent.joinpath(CONFIG_NAME).resolve()


def read_yaml() -> dict:
    """Read yaml configuration file and return dict."""
    with open(CONFIG_PATH) as config_file:
        return yaml.load(config_file, Loader=yaml.FullLoader)


def get_chunksize() -> int:
    """Retrieve standard genie generators chunk size."""
    configdict = read_yaml()
    # TODO handle value error if chunksize not int?
    return int(configdict["chunksize"])


def get_daomgr() -> DaoManager:
    #     # TODO Retrieve from config file
    #     """Configure data mgmt subsystem."""
    #     configdict = read_yaml()
    #     credentials_file = configdict["gbq"]["credentials"]
    #     credentials_path = Path.cwd().joinpath(credentials_file).resolve()
    #     # Google BigQuery Project Name
    #     project_name = "genie-275215"
    #     gbq_dataset = "test"
    #     ctd_dao = daos.CtdDao(
    #         dr.GbqRepository(project_name, CTD_PROPTY, gbq_dataset, credentials_path)
    #     )
    #     # pylint: disable=protected-access
    #     ctd_dao._parser.scraper = mock.MockCtdScraper()
    #     # Create and configure mock pubmed dao
    #     pubmed_dao = daos.PubMedDao(
    #         dr.GbqRepository(project_name, PUBMED_PROPTY, gbq_dataset, credentials_path)
    #     )
    #     # pylint: disable=protected-access
    #     pubmed_dao._parser.scraper = mock.MockPubMedScraper()
    #     # Create and configure mock classifier dao
    #     classifier_dao = daos.ClassifierDao(
    #         dr.GbqRepository(project_name, CLSFR_PROPTY, gbq_dataset, credentials_path)
    #     )
    #     # Construct mock dao manager for testing
    #     daomgr = DaoManager(
    #         ctd_dao=ctd_dao, pubmed_dao=pubmed_dao, classifier_dao=classifier_dao
    #     )
    #     return daomgr
    raise NotImplementedError


def get_classmgr() -> ClassificationMgr:
    #     # TODO Retrieve from config file
    #     """Configure classification mgmt subsystem."""
    #     return mock.MOCK_CLSFRMGR
    raise NotImplementedError
