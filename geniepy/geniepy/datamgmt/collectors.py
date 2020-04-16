"""Collectors manage a parser and database for a given source."""
from abc import ABC, abstractmethod
from pandas import DataFrame
from geniepy.exceptions import SchemaError


class BaseCollector(ABC):
    """Collectors Abstract Base Class."""

    @abstractmethod
    def sync(self):
        """Sync collector database with online sources."""

    @abstractmethod
    def query(self, **kwargs) -> DataFrame:
        """Query collector database."""

    @abstractmethod
    def save(self, payload: DataFrame):
        """
        Save payload to database given data is valid.

        Arguments:
            payload {DataFrame} -- payload to be saved to table

        Raises:
            SchemaError: dataframe does not conform to table schema.
        """
        raise SchemaError


class CtdCollector(BaseCollector):
    """Collectors Abstract Base Class."""

    def sync(self):
        """Sync collector database with online sources."""
        raise NotImplementedError

    def query(self, **kwargs) -> DataFrame:
        """Query collector database."""
        return NotImplementedError

    def save(self, payload: DataFrame):
        """
        Save payload to database given data is valid.

        Arguments:
            payload {DataFrame} -- payload to be saved to table

        Raises:
            SchemaError: dataframe does not conform to table schema.
        """
        raise NotImplementedError
