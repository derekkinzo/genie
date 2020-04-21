"""
Data Access Object Manager.

The DAO manager coordinates the DAOs from each one of the necessary sources to
generate the dataframe usef by the classifiers to calculate a prediction score.
"""
from typing import Generator
import pandas as pd


class DaoManager:
    """
    Implementation of Data Access Object Manager.

    The DAO Manager's objective is to coordinates queries to different DAOs to
    construct the dataframes used by classifiers to calculate prediction scores.
    """

    def gen_records(self) -> Generator[pd.DataFrame, None, None]:
        """
        Generate the dataframe records for classifiers. This function should be called
        after the DAO tables have been created through the download function.

        Returns:
            Generator[pd.DataFrame, None, None] -- Generator of dataframes used by
                classifiers according to the geniepy dataframe schema.
            None -- If DAOs have not downloaded data from online sources and generated
                    internal tables.
        """
        return None
