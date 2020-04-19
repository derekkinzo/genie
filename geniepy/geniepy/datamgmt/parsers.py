"""Data sources parsers."""
from typing import Generator
import hashlib
from abc import ABC, abstractstaticmethod
from enum import Enum, auto
from io import StringIO
import numpy as np
import pandas as pd
from pandas import DataFrame
from pandas_schema import Column, Schema
from pandas_schema.validation import IsDtypeValidation, MatchesPatternValidation
from geniepy import CHUNKSIZE
from geniepy.datamgmt.scrapers import BaseScraper, CtdScraper, PubMedScraper
from geniepy.errors import ParserError


class DataType(Enum):
    """Possible parsable datatypes."""

    CSV = auto()
    XML = auto()


class BaseParser(ABC):
    """Abstract base parser class."""

    scraper: BaseScraper
    schema: Schema
    default_type: DataType = None

    @classmethod
    def validate(cls, payload: DataFrame) -> [str]:
        """
        Check if payload is valid schema.

        Arguments:
            payload {DataFrame} -- The data to be checked against parser schema.

        Returns:
            bool -- true if payload conforms to schema, false otherwise.
        """
        if payload is None:
            return ["Cannot validate None object"]
        return cls.schema.validate(payload)

    @abstractstaticmethod
    def parse(data, dtype: DataType = None) -> DataFrame:
        """
        Parse data and convert according to parser schema.

        Arguments:
            data {Implementation dependent} -- Data to be parsed

        Keyword Arguments:
            dtype {DataType} -- Type of data to be parsed (default: {DataType.CSV})

        Returns:
            DataFrame -- The parsed dataframe.
        """

    @classmethod
    def fetch(cls, chunksize: int = CHUNKSIZE) -> Generator[DataFrame, None, None]:
        """
        Fetch new data, if available from online sources.

        Keyword Arguments:
            chunksize {int} -- the returned generator chunk size (default: {CHUNKSIZE})

        Returns:
            Generator[DataFrame, None, None] -- Generator yielding fetched data
        """
        raw_gen = cls.scraper.scrape(chunksize)
        for data_chunk in raw_gen:
            parsed_df = cls.parse(data_chunk, cls.default_type)
            yield parsed_df


class CtdParser(BaseParser):
    """
    Implementation of CTD Database Parser.

    Comparative Toxicogenomics Gene-Disease Associations Database Parser.
    http://ctdbase.org/
    """

    default_type: DataType = DataType.CSV
    scraper: CtdScraper = CtdScraper()
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
        """
        Parse data and convert according to parser schema.

        Arguments:
            data {Implementation dependent} -- Data to be parsed

        Keyword Arguments:
            dtype {DataType} -- Type of data to be parsed (default: {DataType.CSV})

        Returns:
            DataFrame -- The parsed dataframe.
        """
        parsed_df = pd.read_csv(StringIO(data))
        # Remove unused columns
        parsed_df = parsed_df.drop(
            columns=[
                "DirectEvidence",
                "InferenceChemicalName",
                "InferenceScore",
                "OmimIDs",
            ]
        )
        # Remove prefix 'MESH:' from DiseaseIDs
        parsed_df["DiseaseID"] = parsed_df.apply(
            lambda x: x.DiseaseID.replace("MESH:", ""), axis=1
        )
        # Compute and add the digest
        parsed_df["Digest"] = parsed_df.apply(CtdParser.hash_record, axis=1)
        errors = CtdParser.validate(parsed_df)
        if errors:
            raise ParserError(errors)
        return parsed_df


class PubMedParser(BaseParser):
    """
    Implementation of PubMed Articles Parser.

    https://www.ncbi.nlm.nih.gov/pubmed/
    https://www.nlm.nih.gov/bsd/licensee/elements_descriptions.html
    """

    default_type: DataType = DataType.XML
    scraper: PubMedScraper()
    schema: Schema = Schema(
        [
            Column("pmid", [IsDtypeValidation(np.int64)]),
            Column("date_completed"),
            Column("pub_model"),
            Column("title"),
            Column("iso_abbreviation"),
            Column("article_title"),
            Column("abstract"),
            Column("authors"),
            Column("language"),
            Column("chemicals"),
            Column("mesh_list"),
        ]
    )

    @staticmethod
    def parse(data, dtype: DataType = None) -> DataFrame:
        """
        Parse data and convert according to parser schema.

        Arguments:
            data {Implementation dependent} -- Data to be parsed

        Keyword Arguments:
            dtype {DataType} -- Type of data to be parsed (default: {DataType.CSV})

        Returns:
            DataFrame -- The parsed dataframe.
        """
        return NotImplementedError
