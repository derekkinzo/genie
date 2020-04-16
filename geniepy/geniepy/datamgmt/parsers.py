"""Data sources parsers."""
from pandas import DataFrame
from abc import ABC, abstractstaticmethod


class BaseParser(ABC):
    """Abstract base parser class."""

    @abstractstaticmethod
    def is_valid(payload: DataFrame) -> bool:
        """
        Check if payload is valid schema.

        Arguments:
            payload {DataFrame} -- The data to be checked against parser schema.

        Returns:
            bool -- true if payload conforms to schema, false otherwise.
        """
        if payload is None:
            return False
        raise NotImplementedError


class CtdParser(BaseParser):
    """
    CTD Database Parser.

    Comparative Toxicogenomics Gene-Disease Associations Database Parser.
    http://ctdbase.org/
    """

    @staticmethod
    def is_valid(payload: DataFrame) -> bool:
        """Check if payload is valid ctd schema."""
        return super().is_valid(payload)
