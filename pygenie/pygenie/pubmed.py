"""PubMed related functionality."""
import xml.etree.ElementTree as ET
from datetime import date


class ArticleSetParser():
    """Parsing utility for PubMed Article sets."""


class PubMedArticle():
    """
    PubMed Article model.

    Reference documentation:
    https: // www.nlm.nih.gov/bsd/licensee/elements_descriptions.html
    """

    __slots__ = ['_article_et']

    def __init__(self, article_et: ET.Element):
        """Construct object from corresponding article element tree."""
        self._article_et: ET.Element = article_et

    @property
    def medline_citation(self) -> ET.Element:
        """Retrive medline citation xml sub tree."""
        return self._article_et.find('MedlineCitation')

    @property
    def date_completed(self) -> str:
        """Date completed record distributed to PubMed."""
        date_completed = self.medline_citation.find('DateCompleted')
        year = date_completed.find('Year').text
        month = date_completed.find('Month').text
        day = date_completed.find('Day').text
        return date(int(year), int(month), int(day))
