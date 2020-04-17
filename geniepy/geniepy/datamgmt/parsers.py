"""Data sources parsers."""
from abc import ABC, abstractstaticmethod
import numpy as np
from pandas import DataFrame
from pandas_schema import Column, Schema
from pandas_schema.validation import IsDtypeValidation, MatchesPatternValidation
from enum import Enum, auto


class BaseParser(ABC):
    """Abstract base parser class."""

    schema: Schema = None

    class DataType(Enum):
        """Possible parsable datatypes."""

        DEFAULT = auto()
        CSV = auto()
        STRING = auto()

    @classmethod
    def is_valid(cls, payload: DataFrame) -> bool:
        """
        Check if payload is valid schema.

        Arguments:
            payload {DataFrame} -- The data to be checked against parser schema.

        Returns:
            bool -- true if payload conforms to schema, false otherwise.
        """
        if payload is None:
            return False
        errors: [str] = cls.schema.validate(payload)
        if errors:
            return False
        return True

    @abstractstaticmethod
    def parse(data, data_type: DataType = DataType.DEFAULT) -> DataFrame:
        """
        Parse data and convert according to parser schema.

        Arguments:
            data {Implementation dependent} -- Data to be parsed

        Keyword Arguments:
            type {DataType} -- Type of data to be parsed (default: {DataType.DEFAULT})

        Returns:
            DataFrame -- The parsed dataframe.
        """


class CtdParser(BaseParser):
    """
    Implementation of CTD Database Parser.

    Comparative Toxicogenomics Gene-Disease Associations Database Parser.
    http://ctdbase.org/
    """

    schema: Schema = Schema(
        [
            Column("Digest"),
            Column("GeneSymbol"),
            Column("GeneID", [IsDtypeValidation(np.int64)]),
            Column("DiseaseName"),
            Column(
                "DiseaseID", [MatchesPatternValidation("^D[0-9]+$")]
            ),  # i.e. D000014
            Column("PubMedIDs"),
        ]
    )

    @staticmethod
    def parse(data, data_type=BaseParser.DataType.DEFAULT) -> DataFrame:
        return None

    # I overriding is_valid and computing digest to save computation power
