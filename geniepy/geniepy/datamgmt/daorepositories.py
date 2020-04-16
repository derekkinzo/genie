"""Data Access Repositories to abstract interation with databases."""
from abc import ABC, abstractmethod
from pandas import DataFrame
from geniepy.exceptions import SchemaError


class BaseDaoRepository(ABC):
    """Base Abstract Class for Data Access Object Repositories."""

    @abstractmethod
    def query(self, searchkey: str = "*", **kwargs) -> DataFrame:
        raise SchemaError
