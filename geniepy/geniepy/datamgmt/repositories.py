"""Data Access Repositories to abstract interation with databases."""
from typing import Generator
from abc import ABC, abstractmethod
import pandas as pd
from pandas import DataFrame
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, Float, String
from google.oauth2 import service_account
import pandas_gbq
import geniepy
from geniepy.errors import DaoError


CTD_TABLE_NAME = "ctd"
"""Name of ctd source table."""
CTD_DAO_TABLE = Table(
    CTD_TABLE_NAME,
    MetaData(),
    # No primary key allows duplicate records
    Column("digest", String, primary_key=False, nullable=False),
    Column("genesymbol", String),
    Column("geneid", Integer, nullable=False),
    Column("diseasename", String),
    Column("diseaseid", String, nullable=False),
    Column("pmids", String, nullable=False),
)
"""CTD DAO Repository Schema."""

PUBMED_TABLE_NAME = "pubmed"
"""Name of pubmed source table."""
PUBMED_DAO_TABLE = Table(
    PUBMED_TABLE_NAME,
    MetaData(),
    # No primary key allows duplicate records
    Column("pmid", Integer, primary_key=False, nullable=False),
    Column("date_completed", String),
    Column("pub_model", String),
    Column("title", String),
    Column("iso_abbreviation", String),
    Column("article_title", String),
    Column("abstract", String),
    Column("authors", String),
    Column("language", String),
    Column("chemicals", String),
    Column("mesh_list", String),
)
"""PUBMED DAO Repository Schema."""


CLSFR_TABLE_NAME = "classifier"
"""Name of geniepy classifier output table."""
CLSFR_DAO_TABLE = Table(
    CLSFR_TABLE_NAME,
    MetaData(),
    # No primary key allows duplicate records
    Column("digest", String, primary_key=False, nullable=False),
    Column("pub_score", Float, nullable=False),
    Column("ct_score", Float, nullable=False),
)
"""Classifier Output DAO Repository Schema."""


class BaseRepository(ABC):
    """Base Abstract Class for Data Access Object Repositories."""

    __slots__ = ["_table", "_tablename"]

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
    def delete_all(self):
        """Delete all records in repository."""

    @abstractmethod
    # pylint: disable=bad-continuation
    def query(self, query: str, chunksize: int) -> Generator[DataFrame, None, None]:
        """
        Query DAO repo and returns a generator of DataFrames with query results.

        Keyword Arguments:
            query {str} -- Query string
            chunksize {int} -- Number of rows of dataframe per chunk

        Returns:
            Generator[DataFrame] -- Generator to iterate over DataFrame results.
        """


class SqlRepository(BaseRepository):
    """Implementation of Sqlite Data Access Object Repository."""

    __slots__ = ["_engine"]

    def __init__(self, db_loc: str, tablename: str, table: Table):
        """
        Initialize DAO repository and create table.

        Arguments:
            db_loc {str} -- location of underlying database
            tablename {str} -- the dao table name
            schema {Table} -- the table schema
        """
        self._tablename = tablename
        self._table = table
        # Create sql engine
        self._engine = create_engine(db_loc)
        # Create Table
        self._table.create(self._engine)

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
                self._tablename,
                con=self._engine,
                if_exists="append",
                index=False,
                method="multi",
            )
        except Exception as sql_exp:
            raise DaoError(sql_exp)

    def delete_all(self):
        """Delete all records in repository."""
        self._table.drop(self._engine)
        self._table.create(self._engine)

    # pylint: disable=bad-continuation
    def query(self, query: str, chunksize: int) -> Generator[DataFrame, None, None]:
        """
        Query DAO repo and returns a generator of DataFrames with query results.

        Keyword Arguments:
            query {str} -- Query string
            chunksize {int} -- Number of rows of dataframe per chunk

        Returns:
            Generator[DataFrame] -- Generator to iterate over DataFrame results.
        """
        if query is None:
            return pd.read_sql(self._tablename, con=self._engine, chunksize=chunksize)
        # If query string provided
        generator = pd.read_sql_query(query, self._engine, chunksize=chunksize)
        return generator


class GbqRepository(BaseRepository):  # pragma: no cover
    """Implementation of Sqlite Data Access Object Repository."""

    __slots__ = ["_proj", "_credentials_path"]

    def connect(self):
        """Connect to Google BigQuery."""
        bgq_credentials = service_account.Credentials.from_service_account_file(
            self._credentials_path,
        )
        pandas_gbq.context.credentials = bgq_credentials
        pandas_gbq.context.project = self._proj

    @staticmethod
    def get_dict_schema(table_schema: Table) -> [dict]:
        """Convert Table Schema into GBQ dict expected format."""
        # flake8: noqa
        coldict = lambda col: {
            "name": col.key,
            "type": col.type.__class__.__name__.upper(),
            "mode": "NULLABLE" if col.nullable else "REQUIRED",
        }
        return [coldict(col) for col in table_schema.get_children()]

    def create_table(self):
        """Create table in GBQ."""
        pandas_gbq.to_gbq(
            pd.DataFrame(),
            self.tablename,
            if_exists="replace",
            table_schema=self._table,
        )

    def __init__(self, db_loc: str, tablename: str, table: Table, credentials: str):
        """
        Initialize DAO repository and create table.

        Arguments:
            db_loc {str} -- name of BigQuery project
            tablename {str} -- the dao table name including dataset (i.e. test.table)
            schema {Table} -- the table schema
            credentials_path {str} -- path to gcp credentials json
        """
        self._proj = db_loc
        self._tablename = tablename
        self._table = self.get_dict_schema(table)
        self._credentials_path = credentials
        self.connect()
        self.create_table()

    def save(self, payload: DataFrame):
        """
        Save payload to database table.

        Arguments:
            payload {DataFrame} -- the payload to be stored in db

        Raises:
            DaoError: if cannot save payload to db
        """
        try:
            pandas_gbq.to_gbq(
                payload, self._tablename, if_exists="append", table_schema=self._table,
            )
        except Exception as sql_exp:
            raise DaoError(sql_exp)

    def delete_all(self):
        """Delete all records in repository."""
        self.create_table()

    # pylint: disable=bad-continuation
    def query(self, query: str, chunksize: int) -> Generator[DataFrame, None, None]:
        """
        Query DAO repo and returns a generator of DataFrames with query results.

        Keyword Arguments:
            query {str} -- Query string
            chunksize {int} -- Number of rows of dataframe per chunk

        Returns:
            Generator[DataFrame] -- Generator to iterate over DataFrame results.
        """
        try:
            primary_key = "pmid"
            if query is None:
                query = f"SELECT * FROM {self._tablename} WHERE pmid={primary_key};"
            offset = 0
            # Remove semicolon if exists and add extra params
            query = query.strip(";")
            while True:
                add_query = f" ORDER BY {primary_key} LIMIT {chunksize} OFFSET {offset}"
                gbq_query = query + add_query
                df = pandas_gbq.read_gbq(gbq_query)
                if df.empty:
                    return
                offset += chunksize
                yield df
        except Exception as gbq_exp:
            raise DaoError(gbq_exp)
