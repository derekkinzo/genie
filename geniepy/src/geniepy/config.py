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
import geniepy.datamgmt.tables as gt
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


CONFIGDICT = read_yaml()
PROJNAME = CONFIGDICT["gbq"]["proj"]
DATASET = CONFIGDICT["gbq"]["dataset"]


def get_chunksize() -> int:
    """Retrieve standard genie generators chunk size."""
    configdict = read_yaml()
    # TODO handle value error if chunksize not int?
    return int(configdict["chunksize"])


def get_credentials() -> str:
    """Get credentials file path from config."""
    credentials_file = Path(CONFIGDICT["gbq"]["credentials"]).expanduser()
    credentials_path = Path.cwd().joinpath(credentials_file).resolve()
    if not credentials_path.exists():
        # TODO log error properly
        print(f"Invalid configuration file: {credentials_path}")
        raise ConfigError("Credentials path not found")
    return credentials_path


def get_repos():
    configdict = read_yaml()
    credentials_file = Path(configdict["gbq"]["credentials"]).expanduser()
    credentials_path = Path.cwd().joinpath(credentials_file).resolve()
    projname = configdict["gbq"]["proj"]
    dataset = configdict["gbq"]["dataset"]
    features_repo = dr.GbqRepository(
        projname, gt.FEATURES_PROPTY, "scoring", credentials_path
    )
    scores_repo = dr.GbqRepository(
        projname, gt.SCORES_PROPTY, dataset, credentials_path
    )
    return features_repo, scores_repo


def get_dao(daoname: str):
    dao_dict = {
        "disease2pubtator": (daos.PubtatorDiseaseDao, gt.PUBTATOR_DISEASE_PROPTY,),
        "gene2pubtator": (daos.PubtatorGeneDao, gt.PUBTATOR_GENE_PROPTY),
        "pubmed": (daos.PubMedDao, gt.PUBMED_PROPTY),
    }
    DAO_CLS = dao_dict[daoname][0]
    TABLE_PROPTY = dao_dict[daoname][1]
    credentials = get_credentials()
    dao = DAO_CLS(dr.GbqRepository(PROJNAME, TABLE_PROPTY, DATASET, credentials))
    return dao


def get_daomgr() -> DaoManager:
    """Configure data mgmt subsystem."""
    pubtator_disease_dao = get_dao("disease2pubtator")
    pubtator_gene_dao = get_dao("gene2pubtator")
    pubmed_dao = get_dao("pubmed")
    daomgr = DaoManager(pubtator_disease_dao, pubtator_gene_dao, pubmed_dao)
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
