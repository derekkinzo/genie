"""GeniePy Package entry point."""
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
        "citations": (daos.CitationDao, gt.CITATION_PROPTY),
    }
    DaoClass = dao_dict[daoname][0]
    TABLE_PROPTY = dao_dict[daoname][1]
    credentials = config.get_credentials()
    projname = config.get_projname()
    dataset = config.get_dataset("master")
    dao = DaoClass(dr.GbqRepository(projname, TABLE_PROPTY, dataset, credentials))
    return dao


def create_daomgr() -> DaoManager:
    """Configure data mgmt subsystem."""
    sjr_dao = create_dao("sjr")
    pubtator_disease_dao = create_dao("disease2pubtator")
    pubtator_gene_dao = create_dao("gene2pubtator")
    pubmed_dao = create_dao("pubmed")
    citations_dao = create_dao("citations")

    daomgr = DaoManager(
        sjr_dao=sjr_dao,
        pubtator_disease_dao=pubtator_disease_dao,
        pubtator_gene_dao=pubtator_gene_dao,
        citation_dao=citations_dao,
        pubmed_dao=pubmed_dao,
    )
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


def run_predictions():
    """Calculate predictions for all records in database."""
    features, scores = create_repos()
    classifier = create_classifier()
    query_all = features.query_all
    # Capture initial time and start iterating over relationships
    start_time = time()
    for record_df in features.query(query_all, config.get_chunksize()):
        predicted_df = classifier.predict(record_df)
        scores.save(predicted_df)
        elapsed_time = round(time() - start_time)
        num_records = predicted_df.shape[0]
        print(f"Processed {num_records} in {elapsed_time}s")
        start_time = time()


def update_disease2pubtator():
    """Update pubtator pmid/disease table."""
    disease2pubtator_dao = create_dao("disease2pubtator")
    disease2pubtator_dao.download(config.get_chunksize())


def update_sjr():
    """Update sjr table."""
    sjr_dao = create_dao("sjr")
    sjr_dao.download(config.get_chunksize())


def update_tables():
    """Call scrapes to download data and create/append tables."""
    daomgr: DaoManager = create_daomgr()
    chunksize = config.get_chunksize()
    daomgr.download(chunksize)


def run():
    """Cron-job function to scrape sources for updated data and update predictions."""
    print("Running...")
    print("Done")
