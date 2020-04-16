"""Data sources parsers."""
from pandas import DataFrame
from pandas_schema import Column, Schema
from pandas_schema.validation import IsDtypeValidation, MatchesPatternValidation
from abc import ABC


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


class CtdParser(BaseParser):
    """
    Implementation of CTD Database Parser.

    Comparative Toxicogenomics Gene-Disease Associations Database Parser.
    http://ctdbase.org/
    """

    schema: Schema = Schema(
        [
            Column("GeneSymbol"),
            Column("GeneID", [IsDtypeValidation(int)]),
            Column("DiseaseName"),
            Column("DiseaseID", [MatchesPatternValidation("^D(\d)+$")]),  # i.e. D000014
            # noqa: W605 pylint: disable=all
            Column("PubMedIDs", [IsDtypeValidation(int)]),
        ]
    )
