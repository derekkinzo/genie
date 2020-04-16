"""Data Access Repositories to abstract interation with databases."""
import sqlite3
from abc import ABC, abstractmethod
import pandas as pd
from pandas import DataFrame
from geniepy.errors import SchemaError


class BaseDaoRepo(ABC):
    """Base Abstract Class for Data Access Object Repositories."""

    @abstractmethod
    def query(self, searchkey=None, limit=10e3) -> DataFrame:
        raise SchemaError


class SqliteDaoRepo(BaseDaoRepo):
    """Implementation of Sqlite Data Access Object Repository."""

    def __init__(self):
        """Initialize database."""

    def query(self, searchkey=None, limit=10e3) -> DataFrame:
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
