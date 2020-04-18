"""Data sources parsers."""
from typing import Generator
import hashlib
from abc import ABC, abstractstaticmethod
import numpy as np
import pandas as pd
from pandas import DataFrame
from pandas_schema import Column, Schema
from pandas_schema.validation import IsDtypeValidation, MatchesPatternValidation
from enum import Enum, auto
from geniepy import CHUNKSIZE
from geniepy.datamgmt.scraper import BaseScraper, CtdScraper
from io import StringIO
from geniepy.errors import ParserError


class DataType(Enum):
    """Possible parsable datatypes."""

    CSV = auto()
    XML = auto()


class BaseParser(ABC):
    """Abstract base parser class."""

    schema: Schema = None

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
    def parse(data, dtype: DataType = None) -> DataFrame:
        """
        Parse data and convert according to parser schema.

        Arguments:
            data {Implementation dependent} -- Data to be parsed

        Keyword Arguments:
            dtype {DataType} -- Type of data to be parsed (default: {DataType.DEFAULT})

        Returns:
            DataFrame -- The parsed dataframe.
        """

    @abstractstaticmethod
    def fetch(cls, chunksize: int = CHUNKSIZE) -> Generator[DataFrame, None, None]:
        """
        Fetch new data, if available from online sources

        Keyword Arguments:
            chunksize {int} -- the returned generator chunk size (default: {CHUNKSIZE})

        Returns:
            Generator[DataFrame, None, None] -- Generator yielding fetched data
        """


class CtdParser(BaseParser):
    """
    Implementation of CTD Database Parser.

    Comparative Toxicogenomics Gene-Disease Associations Database Parser.
    http://ctdbase.org/
    """

    scraper: CtdScraper = CtdScraper()
    # TODO Remove "magic strings"
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
    def hash_record(record: pd.Series) -> str:
        """
        Hash the ctd record to generate digest column.

        Arguments:
            record {pd.Series} -- The ctd record in form of pandas Series

        Returns:
            str -- the hex string of the computed digest
        """
        message = str.encode(str(record.GeneID) + record.DiseaseID)
        hexdigest = hashlib.sha256(message).hexdigest()
        return str(hexdigest)

    @staticmethod
    def parse(data, dtype=DataType.CSV) -> DataFrame:
        dataIO = StringIO(data)
        df = pd.read_csv(dataIO)
        # Remove unused columns
        df = df.drop(
            columns=[
                "DirectEvidence",
                "InferenceChemicalName",
                "InferenceScore",
                "OmimIDs",
            ]
        )
        # TODO remove "magic string"
        # Remove prefix 'MESH:' from DiseaseIDs
        df["DiseaseID"] = df.apply(lambda x: x.DiseaseID.replace("MESH:", ""), axis=1)
        # Compute and add the digest
        df["Digest"] = df.apply(CtdParser.hash_record, axis=1)
        df.set_index("Digest")
        if CtdParser.is_valid(df):
            return df
        # Invalid dataframe
        errors: [str] = CtdParser.schema.validate(df)
        raise ParserError("Invalid dataframe %s", errors)

    @classmethod
    def fetch(cls, chunksize: int = CHUNKSIZE) -> Generator[DataFrame, None, None]:
        raw_gen = cls.scraper.scrape(chunksize)
        for data_chunk in raw_gen:
            parsed_df = cls.parse(data_chunk)
            yield parsed_df
