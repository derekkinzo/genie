"""
GeniePy Configuration Module.

This module is intended to provide functions that interprets content from the
package configuration file and generate the corresponding python objects.
"""
from pathlib import Path
import yaml
from geniepy.errors import ConfigError
import geniepy.datamgmt.daos as daos
import geniepy.datamgmt.repositories as dr
from geniepy.datamgmt.tables import (
    PUBMED_PROPTY,
    CTD_PROPTY,
    CLSFR_PROPTY,
    FEATURES_PROPTY,
    SCORES_PROPTY,
)
from geniepy.datamgmt import DaoManager
from geniepy.classmgmt import ClassificationMgr
from geniepy.classmgmt.classifiers import Classifier
from geniepy.classmgmt.classifiers import PCPCLSFR_NAME, CTCLSFR_NAME

CONFIG_NAME = "config.yaml"
DEFAULT_CONFIG = Path(__file__).parent.joinpath(CONFIG_NAME).resolve()
CONFIG_PATH = Path("~/geniepy/config.yaml").expanduser().resolve()


def read_yaml() -> dict:
    """Read yaml configuration file and return dict."""
    with open(CONFIG_PATH) as config_file:
        return yaml.load(config_file, Loader=yaml.FullLoader)


def get_chunksize() -> int:
    """Retrieve standard genie generators chunk size."""
    configdict = read_yaml()
    # TODO handle value error if chunksize not int?
    return int(configdict["chunksize"])


def get_repos():
    configdict = read_yaml()
    credentials_file = Path(configdict["gbq"]["credentials"]).expanduser()
    credentials_path = Path.cwd().joinpath(credentials_file).resolve()
    projname = configdict["gbq"]["proj"]
    dataset = configdict["gbq"]["dataset"]
    features_repo = dr.GbqRepository(
        projname, FEATURES_PROPTY, "scoring", credentials_path
    )
    scores_repo = dr.GbqRepository(projname, SCORES_PROPTY, dataset, credentials_path)
    return features_repo, scores_repo


def get_daomgr() -> DaoManager:
    """Configure data mgmt subsystem."""
    # TODO Retrieve from config file
    configdict = read_yaml()
    credentials_file = Path(configdict["gbq"]["credentials"]).expanduser()
    credentials_path = Path.cwd().joinpath(credentials_file).resolve()
    if not credentials_path.exists():
        # TODO log error properly
        print(f"Invalid configuration file: {credentials_path}")
        raise ConfigError("Credentials path not found")
    # Google BigQuery Project Name
    projname = configdict["gbq"]["proj"]
    dataset = configdict["gbq"]["dataset"]
    # Construct
    ctd_dao = daos.CtdDao(
        dr.GbqRepository(projname, CTD_PROPTY, dataset, credentials_path)
    )
    pubmed_dao = daos.PubMedDao(
        dr.GbqRepository(projname, PUBMED_PROPTY, dataset, credentials_path)
    )
    classifier_dao = daos.ClassifierDao(
        dr.GbqRepository(projname, CLSFR_PROPTY, dataset, credentials_path)
    )
    daomgr = DaoManager(
        ctd_dao=ctd_dao, pubmed_dao=pubmed_dao, classifier_dao=classifier_dao
    )
    return daomgr


def get_classmgr() -> ClassificationMgr:
    """Configure classification mgmt subsystem."""
    # TODO Retrieve from config file
    pub_clsfr = Classifier(PCPCLSFR_NAME)
    ct_clsfr = Classifier(CTCLSFR_NAME)
    clsfr_mgr = ClassificationMgr([pub_clsfr, ct_clsfr])
    return clsfr_mgr


def get_classifier():
    ct_clsfr = Classifier(CTCLSFR_NAME)
    ct_clsfr.load()
    return ct_clsfr
