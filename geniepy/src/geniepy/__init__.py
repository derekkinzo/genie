"""GeniePy Package entry point."""
import os
import sys
import warnings
from concurrent.futures import ProcessPoolExecutor
from itertools import repeat
from pkg_resources import get_distribution, DistributionNotFound
from time import time
import geniepy.config as config
from geniepy.datamgmt import DaoManager
import geniepy.datamgmt.daos as daos
import geniepy.datamgmt.repositories as dr
import geniepy.datamgmt.tables as gt
from geniepy.classmgmt import ClassificationMgr
from geniepy.classmgmt.classifiers import Classifier
from geniepy.classmgmt.classifiers import PCPCLSFR_NAME, CTCLSFR_NAME
from geniepy.errors import ConfigError


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


def create_repos():
    """Configure and create scoring repositories."""
    try:
        credentials = config.get_credentials()
        projname = config.get_projname()
        dataset = config.get_dataset("scoring")
        features_repo = dr.GbqRepository(
            projname, gt.FEATURES_PROPTY, dataset, credentials
        )
        scores_repo = dr.GbqRepository(projname, gt.SCORES_PROPTY, dataset, credentials)
        return features_repo, scores_repo
    except ConfigError as exp:
        print(exp.message)
        exit()


def create_dao(daoname: str):
    """Configure and create Data Access Object."""
    dao_dict = {
        "disease2pubtator": (daos.PubtatorDiseaseDao, gt.PUBTATOR_DISEASE_PROPTY,),
        "gene2pubtator": (daos.PubtatorGeneDao, gt.PUBTATOR_GENE_PROPTY),
        "sjr": (daos.SjrDao, gt.SJR_PROPTY),
        "pubmed": (daos.PubMedDao, gt.PUBMED_PROPTY),
    }
    DAO_CLS = dao_dict[daoname][0]
    TABLE_PROPTY = dao_dict[daoname][1]
    credentials = config.get_credentials()
    projname = config.get_projname()
    dataset = config.get_dataset("master")
    dao = DAO_CLS(dr.GbqRepository(projname, TABLE_PROPTY, dataset, credentials))
    return dao


def create_daomgr() -> DaoManager:
    """Configure data mgmt subsystem."""
    try:
        sjr_dao = create_dao("sjr")
        pubtator_disease_dao = create_dao("disease2pubtator")
        pubtator_gene_dao = create_dao("gene2pubtator")
        pubmed_dao = create_dao("pubmed")
        daomgr = DaoManager(
            sjr_dao, pubtator_disease_dao, pubtator_gene_dao, pubmed_dao
        )
        return daomgr
    except Exception:
        print("Unable to configure Dao Manager")


def create_classmgr() -> ClassificationMgr:
    """Configure classification mgmt subsystem."""
    # TODO Retrieve from config file
    pub_clsfr = Classifier(PCPCLSFR_NAME)
    ct_clsfr = Classifier(CTCLSFR_NAME)
    clsfr_mgr = ClassificationMgr([pub_clsfr, ct_clsfr])
    return clsfr_mgr


def create_classifier():
    """Create classifier obj."""
    ct_clsfr = Classifier(CTCLSFR_NAME)
    ct_clsfr.load()
    return ct_clsfr


def process_records(offset, chunksize, daomgr: DaoManager, classifier: Classifier):
    """Download predict and save records."""
    try:
        pid = os.getpid()
        print(f"Process: {pid} - Downloading {chunksize} features")
        features_df = daomgr.get_features(offset, chunksize)
        if not features_df.empty:
            print(f"Process: {pid} - Calculating {chunksize} predictions")
            predicted_df = classifier.predict(features_df)
            print(f"Process: {pid} - Saving {chunksize} predictions")
            daomgr.save_predictions(predicted_df)
        return True
    except Exception as exp:  # noqa
        sys.stderr.write(
            f"Unable to process records: {offset} to  {offset + chunksize}"
        )
        sys.stderr.write(str(exp))


def run_predictions():
    """Calculate predictions for all records in database."""
    warnings.filterwarnings("ignore")
    daomgr: DaoManager = create_daomgr()
    classifier = create_classifier()
    chunksize = config.get_chunksize()
    start_time = time()
    max_val = daomgr.get_max_feature(chunksize)
    offsets = range(0, max_val, chunksize)
    max_workers = config.get_max_workers()
    outputs = list()
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        for out in executor.map(
            process_records,
            offsets,
            repeat(chunksize),
            repeat(daomgr),
            repeat(classifier),
        ):
            outputs.append(out)
    elapsed_time = round(time() - start_time)
    print(f"Elapsed time: {elapsed_time}s")


def create_tables():
    """Call scrapers to create all tables."""
    daomgr: DaoManager = create_daomgr()
    chunksize = config.get_chunksize()
    daomgr.download(chunksize, baseline=True)


def update_tables():
    """Call scrapes to download data and create/append tables."""
    daomgr: DaoManager = create_daomgr()
    chunksize = config.get_chunksize()
    daomgr.download(chunksize)


def sample_run():
    """Run through entire cycle of creating tables and predictions with sample data."""  # noqa
    daomgr: DaoManager = create_daomgr()
    chunksize = config.get_chunksize()
    daomgr.download(chunksize, is_sample=True, baseline=True)


def init():
    """Create configuration file if doesn't exist."""
    assert config.CONFIG_FILE.exists()
    print(f"GeniePy version {__version__} is ready")
