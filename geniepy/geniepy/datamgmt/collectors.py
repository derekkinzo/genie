"""Collectors manage a parser and database for a given source."""
from typing import Generator
from abc import ABC, abstractmethod
from pandas import DataFrame
from geniepy.errors import SchemaError
from geniepy.datamgmt.parsers import BaseParser, CtdParser
import geniepy.datamgmt.daorepositories as dr


class BaseCollector(ABC):
    """Collectors Abstract Base Class."""

    __slots__ = ["_dao_repo", "_parser"]

    @property
    def tablename(self):
        """Return the dao repo tablename."""
        # pylint: disable=no-member
        return self._dao_repo.tablename

    @abstractmethod
    def sync(self):
        """Sync collector database with online sources."""

    # pylint: disable=bad-continuation
    def query(
        self, query: str = None, chunksize: int = dr.CHUNKSIZE
    ) -> Generator[DataFrame, None, None]:
        """
        Query DAO repo and returns a generator of DataFrames with query results.

        Keyword Arguments:
            query {str} -- Query string. (default: {None} returns all values)
            chunksize {int} -- Number of rows of dataframe per chunk (default: {10e3})

        Returns:
            Generator[DataFrame] -- Generator to iterate over DataFrame results.
        """
        # pylint: disable=no-member
        return self._dao_repo.query(query=query, chunksize=chunksize)

    def save(self, payload: DataFrame):
        """
        Save payload to database given data is valid.

        Arguments:
            payload {DataFrame} -- payload to be saved to table

        Raises:
            SchemaError: dataframe does not conform to table schema.
        """
        # pylint: disable=no-member
        if not self._parser.is_valid(payload):
            raise SchemaError
        self._dao_repo.save(payload)


class CtdCollector(BaseCollector):
    """Implementation of CTD Collector."""

    __slots__ = ["_dao_repo", "_parser"]

    def __init__(self, dao_repo: dr.BaseDaoRepo):
        """Initialize collector state."""
        self._dao_repo = dao_repo
        self._parser = CtdParser()

    def sync(self):
        """Sync collector database with online sources."""
        raise NotImplementedError
