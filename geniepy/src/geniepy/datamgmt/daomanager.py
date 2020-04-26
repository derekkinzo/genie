"""
Data Access Object Manager.

The DAO manager coordinates the DAOs from each one of the necessary sources to
generate the dataframe usef by the classifiers to calculate a prediction score.
"""
from typing import Generator
import pandas as pd
import geniepy.datamgmt.daos as daos


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

    __slots__ = ["_ctd_dao", "_pubmed_dao", "_classifier_dao"]

    # pylint: disable=bad-continuation
    def __init__(
        self,
        ctd_dao: daos.CtdDao,
        pubmed_dao: daos.PubMedDao,
        classifier_dao: daos.ClassifierDao,
    ):
        """Initializa DAO mgr with corresponding DAO children."""
        self._ctd_dao = ctd_dao
        """The CTD DAO handles data from CTD databases."""
        self._pubmed_dao = pubmed_dao
        """The PubMed DAO handles data from PubMed databases."""
        self._classifier_dao = classifier_dao
        """The output DAO stores output data after classifiers calc predictions."""

    def download(self, chunksize: int):
        """Download (scrapes) data for DAOs and creates internal tables."""
        self._ctd_dao.download(chunksize)
        self._pubmed_dao.download(chunksize)

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

    def gen_records(self, chunksize: int) -> Generator[pd.DataFrame, None, None]:
        """
        Generate the dataframe records for classifiers.

        This function should be called after the DAO tables have been created through
        the download function.

        Returns:
            Generator[pd.DataFrame, None, None] -- Generator of dataframes used by
                classifiers according to the geniepy dataframe schema.
            None -- If DAOs have not downloaded data from online sources and generated
                    internal tables.

        Record Schema:
            {
                digest: String,
                genesymbol: String,
                geneid: Integer,
                diseasename: String,
                diseaseid: String,
                pmids: String,
                pubmeds: DataFrame(PubMedParser)
            }
        """
        # iterate over ctd table
        record_df = pd.DataFrame()
        query_all = self._ctd_dao.query_all
        for record_df in self._ctd_dao.query(query_all, chunksize):
            record_df["pubmeds"] = record_df.apply(
                lambda row: self._get_pubmeds_df(row.pmids), axis=1
            )
            yield record_df

    def save_predictions(self, predictions: pd.DataFrame):
        """
        Save computed predictions and supporting data into output tables.

        Arguments:
            records {DataFrame} -- [description]
        """
        self._classifier_dao.save(predictions)
