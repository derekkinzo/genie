"""Data Access Repositories to abstract interation with databases."""
from typing import Generator
from abc import ABC, abstractmethod
import pandas as pd
from datetime import datetime
from pandas import DataFrame
from google.oauth2 import service_account
import pandas_gbq
from sqlalchemy import create_engine, Table
from geniepy.errors import DaoError, ConnectionError
from geniepy.datamgmt.tables import RepoProperties


class BaseRepository(ABC):
    """Base Abstract Class for Data Access Object Repositories."""

    __slots__ = ["_table", "_tablename", "_pkey"]

    @property
    def tablename(self) -> str:
        """Return DAO repo's tablename."""
        # pylint: disable=no-member
        return self._tablename

    @property
    def query_all(self) -> str:
        """Generate query string to query entire table."""
        return f"SELECT * FROM {self.tablename}"

    def query_pkey(self, val) -> str:
        """Generate query string to query by primary key."""
        if isinstance(val, str):
            # pylint: disable=no-member
            return f"SELECT * FROM {self.tablename} WHERE {self._pkey}='{val}'"
        else:
            # Don't need quotes surrounding val if not a str
            # pylint: disable=no-member
            return f"SELECT * FROM {self.tablename} WHERE {self._pkey}={val}"

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
    def query(
        self, query: str, chunksize: int, exact=False
    ) -> Generator[DataFrame, None, None]:
        """
        Query DAO repo and returns a generator of DataFrames with query results.

        Keyword Arguments:
            query {str} -- Query string
            chunksize {int} -- Number of rows of dataframe per chunk
            exact {bool} -- If exact is false, query function manages chunks
                and returns generator. Otherwise, the direct query is returned.

        Returns:
            Generator[DataFrame] -- Generator to iterate over DataFrame results,
                or DataFrame if exact param is True
        """


class SqlRepository(BaseRepository):
    """Implementation of Sqlite Data Access Object Repository."""

    __slots__ = ["_engine"]

    def __init__(self, db_loc: str, propty: RepoProperties):
        """
        Initialize DAO repository and create table.

        Arguments:
            db_loc {str} -- location of underlying database
            propty {RepoProperties} -- Repository properties structure
        """
        self._tablename = propty.tablename
        self._table = propty.table
        self._pkey = propty.pkey
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
    def query(
        self, query: str, chunksize: int, exact=False
    ) -> Generator[DataFrame, None, None]:
        """
        Query DAO repo and returns a generator of DataFrames with query results.

        Keyword Arguments:
            query {str} -- Query string
            chunksize {int} -- Number of rows of dataframe per chunk
            exact {bool} -- If exact is false, query function manages chunks
                and returns generator. Otherwise, the direct query is returned.

        Returny:
            Generator[DataFrame] -- Generator to iterate over DataFrame results.
        """
        if query is None:
            raise DaoError
        # If query string provided
        generator = pd.read_sql_query(query, self._engine, chunksize=chunksize)
        return generator


class GbqRepository(BaseRepository):  # pragma: no cover
    """Implementation of Sqlite Data Access Object Repository."""

    __slots__ = ["_proj", "_credentials_path"]

    # pylint: disable=bad-continuation
    def __init__(
        self, db_loc: str, propty: RepoProperties, dataset: str, credentials: str
    ):
        """
        Initialize DAO repository and create table.

        Arguments:
            db_loc {str} -- name of BigQuery project
            propty {RepoProperties} -- Repository properties structure
            dataset {str} -- The GBQ dataset the table belongs to
            credentials_path {str} -- path to gcp credentials json
        """
        self._proj = db_loc
        self._tablename = dataset + "." + propty.tablename
        self._pkey = propty.pkey
        self._table = self.get_dict_schema(propty.table)
        self._credentials_path = credentials
        self.connect()

    def connect(self):
        """Connect to Google BigQuery."""
        try:
            bgq_credentials = service_account.Credentials.from_service_account_file(
                self._credentials_path,
            )
            pandas_gbq.context.credentials = bgq_credentials
            pandas_gbq.context.project = self._proj
        except Exception as exp:
            raise ConnectionError(exp)

    @staticmethod
    def get_dict_schema(table_schema: Table) -> [dict]:
        """Convert Table Schema into GBQ dict expected format."""
        # flake8: noqa
        if table_schema is None:
            return
        coldict = lambda col: {
            "name": col.key,
            "type": col.type.__class__.__name__.upper(),
            "mode": "NULLABLE" if col.nullable else "REQUIRED",
        }
        return [coldict(col) for col in table_schema.get_children()]

    def save(self, payload: DataFrame):
        """
        Save payload to database table.

        Arguments:
            payload {DataFrame} -- the payload to be stored in db

        Raises:
            DaoError: if cannot save payload to db
        """
        try:
            # Always append date column
            # Todays date
            date = datetime.today().strftime("%Y-%m-%d")
            payload.insert(0, "date", date)
            pandas_gbq.to_gbq(
                payload, self._tablename, if_exists="append", table_schema=self._table,
            )
        except Exception as sql_exp:
            print(f"Exception in {self.tablename}")
            raise DaoError(sql_exp)

    def delete_all(self):
        """Delete all records in repository."""
        pandas_gbq.to_gbq(
            pd.DataFrame(),
            self.tablename,
            if_exists="replace",
            table_schema=self._table,
        )

    # pylint: disable=bad-continuation
    def query(
        self, query: str, chunksize: int, exact=False
    ) -> Generator[DataFrame, None, None]:
        """
        Query DAO repo and returns a generator of DataFrames with query results.

        Keyword Arguments:
            query {str} -- Query string
            chunksize {int} -- Number of rows of dataframe per chunk
            exact {bool} -- If false, query orders results and returns chunks

        Returns:
            Generator[DataFrame] -- Generator to iterate over DataFrame results.
        """
        if query is None:
            raise DaoError
        try:
            if exact:
                response_df = pandas_gbq.read_gbq(query)
                yield response_df
            if not exact:
                offset = 0
                # Remove semicolon if exists in original query to add ordering to query
                query = query.strip(";")
                while True:
                    add_query = (
                        f" ORDER BY {self._pkey} LIMIT {chunksize} OFFSET {offset};"
                    )
                    gbq_query = query + add_query
                    response_df = pandas_gbq.read_gbq(gbq_query)
                    if response_df.empty:
                        return
                    offset += chunksize
                    yield response_df
        except Exception as gbq_exp:
            raise DaoError(gbq_exp)
