"""GeniePy Package entry point."""
import warnings
from concurrent.futures import ProcessPoolExecutor
from itertools import repeat
from tqdm import tqdm
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
    sjr_dao = create_dao("sjr")
    pubtator_disease_dao = create_dao("disease2pubtator")
    pubtator_gene_dao = create_dao("gene2pubtator")
    pubmed_dao = create_dao("pubmed")
    daomgr = DaoManager(sjr_dao, pubtator_disease_dao, pubtator_gene_dao, pubmed_dao)
    return daomgr


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


features, scores = create_repos()
classifier = create_classifier()


def process_records(offset, chunksize):
    gen_query = (
        lambda offset: features.query_all
        + f" WHERE random_num BETWEEN {offset} AND {offset + chunksize};"
    )
    query_str = gen_query(offset)
    print(query_str)
    record_df = next(features.query(query_str, chunksize, exact=True))
    if not record_df.empty():
        predicted_df = classifier.predict(record_df)
        scores.save(predicted_df)


def get_max_record(chunksize):
    count_query = features.query_all.replace("*", "MAX(random_num)")
    max_df = next(features.query(count_query, 1, exact=True))
    # Make sure go past max to include all numbers in range
    return int(max_df.iloc[0][0]) + chunksize


def run_predictions():
    """Calculate predictions for all records in database."""
    warnings.filterwarnings("ignore")
    # Capture initial time and start iterating over relationships
    chunksize = config.get_chunksize()
    start_time = time()
    max_val = get_max_record(chunksize)
    offsets = range(0, max_val, chunksize)
    max_workers = config.get_max_workers()
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        executor.map(process_records, offsets, repeat(chunksize))
    elapsed_time = round(time() - start_time)
    print(f"Elapsed time: {elapsed_time}s")


def update_tables():
    """Call scrapes to download data and create/append tables."""
    daomgr: DaoManager = create_daomgr()
    chunksize = config.get_chunksize()
    daomgr.download(chunksize)


def run():
    """Cron-job function to scrape sources for updated data and update predictions."""
    print("Running...")
    print("Done")
