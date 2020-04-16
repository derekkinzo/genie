"""Collectors manage a parser and database for a given source."""
from abc import ABC, abstractmethod
from pandas import DataFrame
from geniepy.exceptions import SchemaError
from geniepy.datamgmt.daorepositories import BaseDaoRepository
from geniepy.datamgmt.parsers import BaseParser, CtdParser


class BaseCollector(ABC):
    """Collectors Abstract Base Class."""

    dao: BaseDaoRepository
    parser: BaseParser

    @abstractmethod
    def sync(self):
        """Sync collector database with online sources."""

    @abstractmethod
    def query(self, **kwargs) -> DataFrame:
        """Query collector database."""

    def save(self, payload: DataFrame):
        """
        Save payload to database given data is valid.

        Arguments:
            payload {DataFrame} -- payload to be saved to table

        Raises:
            SchemaError: dataframe does not conform to table schema.
        """
        if not self.parser.is_valid(payload):
            raise SchemaError


class CtdCollector(BaseCollector):
    """Collectors Abstract Base Class."""

    def __init__(self):
        """Initialize collector state."""
        self.parser = CtdParser()

    def sync(self):
        """Sync collector database with online sources."""
        raise NotImplementedError

    def query(self, **kwargs) -> DataFrame:
        """Query collector database."""
        return NotImplementedError
