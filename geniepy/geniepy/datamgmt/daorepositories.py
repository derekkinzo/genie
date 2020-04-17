"""Data Access Repositories to abstract interation with databases."""
import sqlite3
from typing import Generator
from abc import ABC, abstractmethod
import pandas as pd
from pandas import DataFrame
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from geniepy.errors import DaoError
from geniepy.datamgmt.parsers import BaseParser, CtdParser


CHUNKSIZE: int = 10 ** 4
"""Standard generator chunk size for DAO queries."""


class BaseDaoRepo(ABC):
    """Base Abstract Class for Data Access Object Repositories."""

    @property
    def tablename(self):
        """Return DAO repo's tablename."""
        return self._tablename

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
    def query(
        self, query: str = None, chunksize: int = CHUNKSIZE
    ) -> Generator[DataFrame, None, None]:
        """
        Query DAO repo and returns a generator of DataFrames with query results.

        Keyword Arguments:
            query {str} -- Query string. (default: {None} returns all values)
            chunksize {int} -- Number of rows of dataframe per chunk (default: {10e3})

        Returns:
            Generator[DataFrame] -- Generator to iterate over DataFrame results.
        """


class SqlDaoRepo(BaseDaoRepo):
    """Implementation of Sqlite Data Access Object Repository."""

    def create_table(self):
        """Create database table."""
        user_table = Table(
            self._tablename,
            self._metadata,
            Column("Digest", String, primary_key=True, nullable=False),
            Column("GeneSymbol", String),
            Column("GeneID", Integer, nullable=False),
            Column("DiseaseName", String),
            Column("DiseaseID", String, nullable=False),
            Column("PubMedIDs", String, nullable=False),
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

    def query(
        self, query: str = None, chunksize: int = CHUNKSIZE
    ) -> Generator[DataFrame, None, None]:
        """
        Query DAO repo and returns a generator of DataFrames with query results.

        Keyword Arguments:
            query {str} -- Query string. (default: {None} returns all values)
            chunksize {int} -- Number of rows of dataframe per chunk (default: {10e3})

        Returns:
            Generator[DataFrame] -- Generator to iterate over DataFrame results.
        """
        if query is None:
            return pd.read_sql(self._tablename, con=self._engine, chunksize=chunksize)
        # If query string provided
        generator = pd.read_sql_query(query, self._engine, chunksize=chunksize)
        return generator
