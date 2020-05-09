"""
Data Access Object Manager.

The DAO manager coordinates the DAOs from each one of the necessary sources to
generate the dataframe usef by the classifiers to calculate a prediction score.
"""
from typing import Generator
import pandas as pd
import geniepy.datamgmt.daos as daos
from multiprocessing import Process
import geniepy.config as config
import geniepy.datamgmt.tables as gt
import geniepy.datamgmt.repositories as dr


class DaoManager:
    """
    Implementation of Data Access Object Manager.

    The DAO manager is intended to utilize different DAOs to generate
    dataframe records used by the classifiers.

    At start of day the download method should be called to scrape data from online
    sources on each DAO and generate appropriate tables.

    The DAO manager should then be called to generate the records that can be fed into
    the classifiers.
    """

    __slots__ = [
        "_sjr_dao",
        "_pubtator_disease_dao",
        "_pubtator_gene_dao",
        "_pubmed_dao",
        "_features",
        "_scores",
    ]

    def create_repos(self):
        """Configure and create scoring repositories."""
        credentials = config.get_credentials()
        projname = config.get_projname()
        dataset = config.get_dataset("scoring")
        features_repo = dr.GbqRepository(
            projname, gt.FEATURES_PROPTY, dataset, credentials
        )
        scores_repo = dr.GbqRepository(projname, gt.SCORES_PROPTY, dataset, credentials)
        return features_repo, scores_repo

    # pylint: disable=bad-continuation
    def __init__(
        self,
        sjr_dao: daos.SjrDao,
        pubtator_disease_dao: daos.PubtatorDiseaseParser,
        pubtator_gene_dao: daos.PubtatorGeneParser,
        pubmed_dao: daos.PubMedDao,
    ):
        """Initializa DAO mgr with corresponding DAO children."""
        self._sjr_dao = sjr_dao
        self._pubtator_disease_dao = pubtator_disease_dao
        self._pubtator_gene_dao = pubtator_gene_dao
        self._pubmed_dao = pubmed_dao
        self._features, self._scores = self.create_repos()

    def download(self, chunksize: int, **kwargs):
        """Download (scrapes) data for DAOs and creates internal tables."""
        # Fire off scrapers async
        psjr = Process(target=self._sjr_dao.download, args=(chunksize,), kwargs=kwargs)
        ppubtatordisease = Process(
            target=self._pubtator_disease_dao.download, args=(chunksize,), kwargs=kwargs
        )
        ppubtatorgene = Process(
            target=self._pubtator_gene_dao.download, args=(chunksize,), kwargs=kwargs
        )
        ppubmed = Process(
            target=self._pubmed_dao.download, args=(chunksize,), kwargs=kwargs
        )
        psjr.start()
        ppubtatordisease.start()
        ppubtatorgene.start()
        ppubmed.start()

    def _get_pubmeds_df(self, pmids: str):
        """
        Get pubmed dao dataframes.

        Arguments:
            pubmeds {str} -- pipe delimtied string with pmids
            chunksize {int} -- limits max chunksize internally to limit memory usage

        Returns: Dataframe with pubmed dao dataframe.
        """
        pmids = pmids.split("|")
        pubmed_df = pd.DataFrame()
        for pmid in pmids:
            try:
                pmid_query = self._pubmed_dao.query_pkey(int(pmid))
                # Only care about 1 pmid entry (table shouldn't have duplicates)
                pmid_df = next(self._pubmed_dao.query(pmid_query, 1))
                pubmed_df = pubmed_df.append(pmid_df, ignore_index=True)
            except StopIteration:  # pragma: no cover
                # TODO log instead of print
                print(f"PMID: {pmid} not found!")
        return pubmed_df

    def get_max_feature(self, chunksize):
        """Retrieve the max addressable record in features table."""
        count_query = self._features.query_all.replace("*", "MAX(random_num)")
        max_df = next(self._features.query(count_query, 1, exact=True))
        # Make sure go past max to include all numbers in range
        return int(max_df.iloc[0][0]) + chunksize

    def get_features(self, offset: int, chunksize: int) -> pd.DataFrame:
        """
        Generate the dataframe records for classifiers.

        This function should be called after the DAO tables have been created through
        the download function.

        Arguments:
            offset {int} -- The offset of records to be fetched
            chunksize {int} -- The number of records to be returned


        Returns:
            A dataframe containing records from features table
        """
        gen_query = (
            lambda offset: self._features.query_all
            + f" WHERE random_num BETWEEN {offset} AND {offset + chunksize};"
        )
        query_str = gen_query(offset)
        print(query_str)
        record_df = next(self._features.query(query_str, chunksize, exact=True))
        return record_df

    def save_predictions(self, predictions: pd.DataFrame):
        """
        Save computed predictions and supporting data into output tables.

        Arguments:
            records {DataFrame} -- [description]
        """
        self._scores.save(predictions)
