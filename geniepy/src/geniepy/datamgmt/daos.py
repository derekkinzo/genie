"""
Data Access Managers Module.

DAOs are responsible for scraping, parsing, storing and delivering a specific type of
data. i.e. Pubmed Publications, Clinical Trials, Gene-Disease Relationships.
"""
from typing import Generator
from abc import ABC
from pandas import DataFrame
from geniepy.errors import SchemaError
from geniepy.datamgmt.parsers import (
    BaseParser,
    CtdParser,
    PubMedParser,
    ClassifierParser,
    PubtatorGeneParser,
    PubtatorDiseaseParser,
    SjrParser,
)
import geniepy.datamgmt.repositories as dr


class BaseDao(ABC):
    """
    Data Access Object Abstract Base Class.

    Each DAO is composed of one or more repositories and a parser which is used to
    structure and validate the DAO's data. Consult the parser's schema to check the
    format of the data stored in the repositories.
    """

    _repository: dr.BaseRepository
    """Database repository used by DAO to store objects."""
    _parser: BaseParser
    """DAO's parser to scraping and validating data."""

    def __init__(self, repository: dr.BaseRepository):
        """Initialize DAO state."""
        self._repository = repository

    @property
    def query_all(self):
        """Generate query string to query entire table."""
        return self._repository.query_all

    def query_pkey(self, val) -> str:
        """
        Generate query by primary key string.

        Arguments:
            val  -- value of primary key

        Returns:
            str -- The query str
        """
        return self._repository.query_pkey(val)

    def download(self, chunksize: int, **kwargs):
        """
        Download new data from online sources if available.

        Keyword Arguments:
            chunksize {[type]} -- The download method can be very computationally and
            memory intentive since it could possibly need to download and parse all
            records if the tables are empty. The chunksize allows the caller to limit
            how much memory is processed at a time while downloading and parsing the
            data.
        """
        for chunk_df in self._parser.fetch(chunksize, **kwargs):
            self._repository.save(chunk_df)

    def purge(self):
        """Purge all dao's database records."""
        self._repository.delete_all()

    # pylint: disable=bad-continuation
    def query(self, query: str, chunksize: int) -> Generator[DataFrame, None, None]:
        """
        Query DAO repo and returns a generator of DataFrames with query results.

        Keyword Arguments:
            query {str} -- Query string.
            chunksize {int} -- Number of rows of dataframe per chunk

        Returns:
            Generator[DataFrame] -- Generator to iterate over DataFrame results.
        """
        # pylint: disable=no-member
        return self._repository.query(query=query, chunksize=chunksize)

    def save(self, payload: DataFrame):
        """
        Save payload to database given data is valid.

        Arguments:
            payload {DataFrame} -- payload to be saved to table

        Raises:
            SchemaError: dataframe does not conform to table schema.
        """
        # pylint: disable=no-member
        errors = self._parser.validate(payload)
        if errors:
            raise SchemaError
        self._repository.save(payload)

    @property
    def tablename(self):
        """Return the dao repo tablename."""
        # pylint: disable=no-member
        return self._repository.tablename


class CtdDao(BaseDao):
    """Implementation of CTD Data Access Object."""

    __slots__ = ["_repository"]

    _parser: CtdParser = CtdParser()


class PubMedDao(BaseDao):
    """Implementation of CTD Data Access Object."""

    __slots__ = ["_repository"]

    _parser: PubMedParser = PubMedParser()


class ClassifierDao(BaseDao):
    """Implementation of DAO to handle output data used by UI for visualizations."""

    __slots__ = ["_repository"]

    _parser: ClassifierParser = ClassifierParser()

    def download(self, chunksize):
        """Classifiers don't need scrapers, so method not implemented."""
        raise NotImplementedError


class PubtatorGeneDao(BaseDao):
    """Data Access Object for Pubtator PMID/GeneID records."""

    __slots__ = ["_repository"]

    _parser: PubtatorGeneParser = PubtatorGeneParser()


class PubtatorDiseaseDao(BaseDao):
    """Data Access Object for Pubtator PMID/DiseaseID records."""

    __slots__ = ["_repository"]

    _parser: PubtatorDiseaseParser = PubtatorDiseaseParser()


class SjrDao(BaseDao):
    """Data Access Object for Pubtator PMID/DiseaseID records."""

    __slots__ = ["_repository"]

    _parser: SjrParser = SjrParser()
