"""Data Access Repositories to abstract interation with databases."""
from abc import ABC, abstractmethod
from pandas import DataFrame
from geniepy.errors import SchemaError


class BaseDaoRepo(ABC):
    """Base Abstract Class for Data Access Object Repositories."""

    @abstractmethod
    def query(self, searchkey: str = "*", **kwargs) -> DataFrame:
        raise SchemaError


class SqliteDaoRepo(BaseDaoRepo):
    """Implementation of Sqlite Data Access Object Repository."""

    @abstractmethod
    def query(self, searchkey: str = "*", **kwargs) -> DataFrame:
        raise SchemaError
