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
import geniepy.datamgmt.scrapers as gs
from geniepy.errors import ParserError
from geniepy.pubmed import PubMedArticle
from geniepy.classmgmt.classifiers import PCPCLSFR_NAME, CTCLSFR_NAME


class DataType(Enum):
    """Possible parsable datatypes."""

    CSV_STR = auto()  # csv string
    XML = auto()  # xml element tree
    DF = auto()  # pandas dataframe


class BaseParser(ABC):
    """Abstract base parser class."""

    scraper: gs.BaseScraper
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

    def fetch(self, chunksize: int, **kwargs) -> Generator[DataFrame, None, None]:
        """
        Fetch new data, if available from online sources.

        Keyword Arguments:
            chunksize {int} -- the returned generator chunk size

        Returns:
            Generator[DataFrame, None, None] -- Generator yielding fetched data
        """
        raw_gen = self.scraper.scrape(chunksize, **kwargs)

        # for testing purposes only - returns single yield
        if "is_sample" in kwargs and kwargs.get("is_sample") == True:
            parsed_df = self.parse(next(raw_gen), self.default_type)
            yield parsed_df
            return

        # for production purposes - iterate through yields
        for data_chunk in raw_gen:
            parsed_df = self.parse(data_chunk, self.default_type)
            yield parsed_df


class CtdParser(BaseParser):
    """
    Implementation of CTD Database Parser.

    Comparative Toxicogenomics Gene-Disease Associations Database Parser.
    http://ctdbase.org/
    """

    default_type: DataType = DataType.CSV_STR
    scraper: gs.CtdScraper = gs.CtdScraper()
    schema: Schema = Schema(
        [
            Column("digest"),
            Column("genesymbol"),
            Column("geneid", [IsDtypeValidation(np.int64)]),
            Column("diseasename"),
            Column(
                "diseaseid", [MatchesPatternValidation("^D[0-9]+$")]
            ),  # i.e. D000014
            Column("pmids"),
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
        message = str.encode(str(record.geneid) + record.diseaseid)
        hexdigest = hashlib.sha256(message).hexdigest()
        return str(hexdigest)

    @staticmethod
    def parse(data, dtype=DataType.CSV_STR) -> DataFrame:
        """
        Parse data and convert according to parser schema.

        Arguments:
            data {Implementation dependent} -- Data to be parsed

        Keyword Arguments:
            dtype {DataType} -- Type of data to be parsed (default: {DataType.CSV})

        Returns:
            DataFrame -- The parsed dataframe.

        Raises:
            ParserError -- If unable to parse data
        """
        try:
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
            # Rename columns based on schema
            parsed_df.rename(
                columns={
                    "GeneSymbol": "genesymbol",
                    "GeneID": "geneid",
                    "DiseaseName": "diseasename",
                    "DiseaseID": "diseaseid",
                    "PubMedIDs": "pmids",
                },
                inplace=True,
            )
            # Compute and add the digest
            parsed_df["digest"] = parsed_df.apply(CtdParser.hash_record, axis=1)
            errors = CtdParser.validate(parsed_df)
            if errors:
                raise ParserError(errors)
            return parsed_df
        except Exception as parse_exp:
            raise ParserError(parse_exp)


class PubtatorDiseaseParser(BaseParser):
    """Implementation of Pubtator Disease Parser."""

    default_type: DataType = DataType.DF
    scraper: gs.PubtatorDiseaseScraper = gs.PubtatorDiseaseScraper()

    @staticmethod
    def parse(data, dtype=DataType.DF) -> DataFrame:
        """Parse data and convert according to parser schema."""
        try:
            parsed_df = data[["PMID", "DiseaseID"]].copy()
            return parsed_df
        except:
            return None


class PubtatorGeneParser(BaseParser):
    """Implementation of Pubtator Gene Parser."""

    default_type: DataType = DataType.DF
    scraper: gs.PubtatorGeneScraper = gs.PubtatorGeneScraper()

    @staticmethod
    def parse(data, dtype=DataType.DF) -> DataFrame:
        """Parse data and convert according to parser schema."""
        try:
            parsed_df = data[["PMID", "GeneID"]].copy()
            return parsed_df
        except:
            return None


class SjrParser(BaseParser):
    """Implementation of Scientific Journal Ratings Parser."""

    default_type: DataType = DataType.DF
    scraper: gs.SjrScraper = gs.SjrScraper()

    @staticmethod
    def parse(data, dtype=DataType.DF) -> DataFrame:
        """Parse data and convert according to parser schema."""
        try:
            parsed_df = data[["Title", "SJR", "H index"]].copy()
            parsed_df.rename(columns={"H index": "h_index"}, inplace=True)
            return parsed_df
        except:
            return None


class PubMedParser(BaseParser):
    """
    Implementation of PubMed Articles Parser.

    https://www.ncbi.nlm.nih.gov/pubmed/
    https://www.nlm.nih.gov/bsd/licensee/elements_descriptions.html
    """

    default_type: DataType = DataType.XML
    scraper: gs.PubMedScraper = gs.PubMedScraper()
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
            Column("issn"),
            Column("issn_type"),
            Column("citation_count"),
            Column("citation_pmid"),
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
        # Data passed in should be a list of xml element trees
        # xml_list = data
        articles = data

        # The keys of the dataframe
        keys = [
            "pmid",
            "date_completed",
            "pub_model",
            "title",
            "iso_abbreviation",
            "article_title",
            "abstract",
            "authors",
            "language",
            "chemicals",
            "mesh_list",
            "issn",
            "issn_type",
            "citation_count",
            "citation_pmid",
        ]

        # Temp array variables to store from each xml element tree
        pmid_list = []
        date_completed_list = []
        pub_model_list = []
        title_list = []
        iso_abbreviation_list = []
        article_title_list = []
        abstract_list = []
        authors_list = []
        language_list = []
        chemicals_list = []
        mesh_list_list = []
        issn_list = []
        issn_type_list = []
        citation_count_list = []
        citation_pmid_list = []

        try:
            # General XML Tags
            # for xml_article in xml_list:
            for article in articles:
                # article = PubMedArticle(xml_article)
                pmid_list.append(np.int64(article.pmid))
                date_completed_list.append(article.date_completed)
                pub_model_list.append(article.pub_model)
                title_list.append(article.title)
                iso_abbreviation_list.append(article.iso_abbreviation)
                article_title_list.append(article.article_title)
                abstract_list.append(article.abstract)
                authors_list.append(str(article.authors).strip("[]"))
                language_list.append(article.language)
                chemicals_list.append(str(article.chemicals).strip("[]"))
                mesh_list_list.append(str(article.mesh_list).strip("[]"))
                issn_list.append(str(article.issn).strip("[]"))
                issn_type_list.append(str(article.issn_type).strip("[]"))
                citation_count_list.append(str(article.citationCount).strip("[]"))
                citation_pmid_list.append(str(article.citationPmid).strip("[]"))

            # Create the array of arrays of values in dataframe
            values = [
                pmid_list,
                date_completed_list,
                pub_model_list,
                title_list,
                iso_abbreviation_list,
                article_title_list,
                abstract_list,
                authors_list,
                language_list,
                chemicals_list,
                mesh_list_list,
                issn_list,
                issn_type_list,
                citation_count_list,
                citation_pmid_list,
            ]

            # Zip df keys and values and create dataframe
            zipped = list(zip(keys, values))
            parsed_df = pd.DataFrame(dict(zipped))

            errors = PubMedParser.validate(parsed_df)
            if errors:
                raise ParserError(errors)  # pragma: no cover - should never reach
            return parsed_df
        except Exception as parse_exp:
            raise ParserError(parse_exp)


class ClassifierParser(BaseParser):
    """
    Implementation of classifier dao Parser.

    The classifier output tables contain the output data from geniepy after the
    classifiers have calculated desired predictions.
    """

    default_type: DataType = None
    scraper: None
    """No online sources for classifiers output."""
    schema: Schema = Schema(
        [
            Column("digest"),
            Column(PCPCLSFR_NAME, [IsDtypeValidation(np.float64)]),
            Column(CTCLSFR_NAME, [IsDtypeValidation(np.float64)]),
        ]
    )

    def fetch(self, chunksize: int) -> Generator[DataFrame, None, None]:
        """No online sources to fetch from for classifiers outputs."""
        raise NotImplementedError("Classifier Output Parser has no Scrapers")

    @staticmethod
    def parse(data, dtype=DataType.CSV_STR) -> DataFrame:
        """
        Parser function from base class.

        Raises:
            NotImplementedError -- Function not implemented since classifiers return
                dataframes that only need to be validated.
        """
        raise NotImplementedError("Classifier Output Parser has no Scrapers")
