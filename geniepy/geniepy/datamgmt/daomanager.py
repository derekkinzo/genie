"""
Data Access Object Manager.

The DAO manager coordinates the DAOs from each one of the necessary sources to
generate the dataframe usef by the classifiers to calculate a prediction score.
"""
from typing import Generator
import pandas as pd
import geniepy.datamgmt.daos as daos
from geniepy import CHUNKSIZE


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

    __slots__ = ["_ctd_dao", "_pubmed_dao"]

    def __init__(self, ctd_dao: daos.CtdDao, pubmed_dao: daos.PubMedDao):
        """Initializa DAO mgr with corresponding DAO children."""
        self._ctd_dao = ctd_dao
        self._pubmed_dao = pubmed_dao

    def download(self):
        """Download (scrapes) data for DAOs and creates internal tables."""
        self._ctd_dao.download()
        self._pubmed_dao.download()

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
            pmid_query = (
                f"SELECT * FROM {self._pubmed_dao.tablename} WHERE pmid='{pmid}';"
            )
            try:
                # Only care about 1 pmid entry (table shouldn't have duplicates)
                pmid_gen = self._pubmed_dao.query(pmid_query, 1)
                pmid_df = next(pmid_gen)
                pubmed_df = pubmed_df.append(pmid_df)
            except StopIteration:
                # TODO log instead of print
                print(f"PMID: {pmid} not found!")
        return pubmed_df

    def gen_records(self, chunksize=CHUNKSIZE) -> Generator[pd.DataFrame, None, None]:
        """
        Generate the dataframe records for classifiers.

        This function should be called after the DAO tables have been created through
        the download function.

        Returns:
            Generator[pd.DataFrame, None, None] -- Generator of dataframes used by
                classifiers according to the geniepy dataframe schema.
            None -- If DAOs have not downloaded data from online sources and generated
                    internal tables.
        """
        # iterate over ctd table
        record_keys = ["gene", "disease", "pubmeds", "stages"]
        genes = []
        diseases = []
        pubmeds = []
        stages = []
        for ctd_df in self._ctd_dao.query(chunksize=chunksize):
            for _, row in ctd_df.iterrows():
                genes.append(row.gene)
                pubmeds.append(self._get_pubmeds_df(row.PubMedIDs))
                print(pubmeds)
        record_vals = [genes, diseases, pubmeds, stages]
        record_df = pd.DataFrame(dict(zip(record_keys, record_vals)))
        return record_df
