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
    def date_completed(self) -> date:
        """Date completed record distributed to PubMed."""
        date_completed = self.medline_citation.find('DateCompleted')
        year = int(date_completed.find('Year').text)
        month = int(date_completed.find('Month').text)
        day = int(date_completed.find('Day').text)
        return date(year, month, day)

    @property
    def pub_model(self) -> str:
        """Publication model - medium/media in which article was published."""
        raise NotImplementedError

    @property
    def date_pub(self) -> date:
        """Full date on which issue was published."""
        # consider removing - not standard format
        raise NotImplementedError

    @property
    def title(self) -> str:
        """The full journal title."""
        raise NotImplementedError

    @property
    def iso_abbreviation(self) -> str:
        """The journal title ISO abbreviation."""
        raise NotImplementedError

    @property
    def article_title(self) -> str:
        """Entire title of journal article in English."""
        raise NotImplementedError

    @property
    def abstract(self) -> str:
        """Entire abstract taken directly from published article."""
        raise NotImplementedError

    @property
    def authors(self) -> [str]:
        """Names of authors published with article."""
        raise NotImplementedError

    @property
    def language(self) -> str:
        """Tha language the article was published in."""
        raise NotImplementedError

    @property
    def chemicals(self) -> [str]:
        """One or more chemical elements."""
        raise NotImplementedError

    @property
    def mesh_list(self) -> [str]:
        """Article's suppl mesh list."""
        raise NotImplementedError

    @property
    def to_dict(self):
        """Generate article model dictionary."""
        obj_dict = {}
        obj_dict['date_completed'] = str(self.date_completed)
        raise NotImplementedError
        return obj_dict
