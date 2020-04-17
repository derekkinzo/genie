"""Data Access Repositories to abstract interation with databases."""
import sqlite3
from abc import ABC, abstractmethod
import pandas as pd
from pandas import DataFrame
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from geniepy.errors import DaoError
from geniepy.datamgmt.parsers import BaseParser, CtdParser


class BaseDaoRepo(ABC):
    """Base Abstract Class for Data Access Object Repositories."""

    @abstractmethod
    def save(self, df: DataFrame):
        """
        Save payload to database table.

        Arguments:
            df {DataFrame} -- the payload to be saved to the table as a pandas DataFrame

        Raises:
            DaoError: if cannot save payload to db
        """

    @abstractmethod
    def query(self, searchkey=None, chunksize=10e3) -> DataFrame:
        pass


class SqliteDaoRepo(BaseDaoRepo):
    """Implementation of Sqlite Data Access Object Repository."""

    def create_table(self):
        """Create database table."""
        user_table = Table(
            self._tablename,
            self._metadata,
            Column("Digest", String, primary_key=True, nullable=False),
            Column("GeneSymbol", String),
            Column("GeneID", Integer),
            Column("DiseaseName", String),
            Column("DiseaseID", String),
            Column("PubMedIDs", String),
        )
        user_table.create(self._engine)

    def __init__(self, db_loc: str, tablename: str):
        """Initialize database."""
        self._engine = create_engine(db_loc)
        self._metadata = MetaData()
        self._tablename = tablename
        self.create_table()

    def save(self, df: DataFrame):
        """
        Save payload to database table.

        Arguments:
            df {DataFrame} -- the payload to be saved to the table as a pandas DataFrame

        Raises:
            DaoError: if cannot save payload to db
        """
        try:
            df.to_sql(
                self._tablename, con=self._engine, if_exists="append", index=False
            )
        except Exception as sql_exp:
            raise DaoError(sql_exp)

    def query(self, searchkey=None, chunksize=10e3) -> DataFrame:
        return pd.DataFrame(
            {
                "Digest": [22659286],
                "GeneSymbol": ["11-BETA-HSD3"],
                "GeneID": [100174880],
                "DiseaseName": ["Abnormalities, Drug-Induced"],
                "DiseaseID": ["D000014"],
                "PubMedIDs": [22659286],
            }
        )
