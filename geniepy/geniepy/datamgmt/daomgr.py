"""
Data Access Object Manager.

The DAO manager coordinates the DAOs from each one of the necessary sources to
generate the dataframe usef by the classifiers to calculate a prediction score.
"""
from typing import Generator, NamedTuple
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
        for ctd_df in self._ctd_dao.query(chunksize=chunksize):
            for index, row in ctd_df.iterrows():
                print(row)
