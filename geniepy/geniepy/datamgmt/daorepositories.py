"""Data Access Repositories to abstract interation with databases."""
from typing import Generator
from abc import ABC, abstractmethod
import pandas as pd
from pandas import DataFrame
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from geniepy.errors import DaoError


CHUNKSIZE: int = 10 ** 4
"""Standard generator chunk size for DAO queries."""

CTD_TABLE_NAME = "ctd"
"""Name of ctd source table."""
CTD_DAO_SCHEMA = Table(
    CTD_TABLE_NAME,
    MetaData(),
    Column("Digest", String, primary_key=True, nullable=False),
    Column("GeneSymbol", String),
    Column("GeneID", Integer, nullable=False),
    Column("DiseaseName", String),
    Column("DiseaseID", String, nullable=False),
    Column("PubMedIDs", String, nullable=False),
)
"""CTD DAO Repository Schema."""


class BaseDaoRepo(ABC):
    """Base Abstract Class for Data Access Object Repositories."""

    __slots__ = ["_tablename"]

    @property
    def tablename(self):
        """Return DAO repo's tablename."""
        return self._tablename  # pylint: disable=E1101

    @abstractmethod
    def save(self, payload: DataFrame):
        """
        Save payload to database table.

        Arguments:
            payload {DataFrame} -- the payload to be stored in db

        Raises:
            DaoError: if cannot save payload to db
        """

    @abstractmethod
    # pylint: disable=bad-continuation
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

    __slots__ = ["_tablename", "_engine"]

    def create_table(self, schema: Table):
        """Create database table."""
        table = schema
        table.create(self._engine)

    def __init__(self, db_loc: str, tablename: str, schema: Table):
        """
        Initialize DAO repository and create table.

        Arguments:
            db_loc {str} -- location of underlying database
            tablename {str} -- the dao table name
            schema {Table} -- the table schema
        """
        self._engine = create_engine(db_loc)
        self._tablename = tablename
        self.create_table(schema)

    def save(self, payload: DataFrame):
        """
        Save payload to database table.

        Arguments:
            payload {DataFrame} -- the payload to be stored in db

        Raises:
            DaoError: if cannot save payload to db
        """
        try:
            payload.to_sql(
                self._tablename, con=self._engine, if_exists="append", index=False
            )
        except Exception as sql_exp:
            raise DaoError(sql_exp)

    # pylint: disable=bad-continuation
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
