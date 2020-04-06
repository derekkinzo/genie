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
    def _medline_element(self) -> ET.Element:
        """Retrive medline sub element from pubmedarticle."""
        return self._article_et.find('MedlineCitation')

    @property
    def _article_element(self) -> ET.Element:
        """Retrieve article sub element medline."""
        return self._medline_element.find('Article')

    @property
    def _journal_element(self) -> ET.Element:
        """Retrieve journal sub element article."""
        return self._article_element.find("Journal")

    @property
    def pmid(self) -> str:
        """Pubmed article ID."""
        pmid = self._medline_element.find('PMID')
        return pmid.text

    @property
    def date_completed(self) -> date:
        """Date completed record distributed to PubMed."""
        # TODO need to ensure consistent date format across, probably best to change implementation and return str
        date_completed = self._medline_element.find('DateCompleted')
        year = int(date_completed.find('Year').text)
        month = int(date_completed.find('Month').text)
        day = int(date_completed.find('Day').text)
        return date(year, month, day)

    @property
    def pub_model(self) -> str:
        """Publication model - medium/media in which article was published."""
        article = self._article_element
        pub_model = article.attrib['PubModel']
        return pub_model

    @property
    def title(self) -> str:
        """Full journal title."""
        journal = self._journal_element
        title = journal.find('Title')
        return title.text

    @property
    def iso_abbreviation(self) -> str:
        """Journal title ISO abbreviation."""
        iso_abbrev = self._journal_element.find('ISOAbbreviation')
        return iso_abbrev.text

    @property
    def article_title(self) -> str:
        """Entire title of journal article in English."""
        article_title = self._article_element.find('ArticleTitle')
        return article_title.text

    @property
    def abstract(self) -> str:
        """Entire abstract taken directly from published article."""
        abstract = self._article_element.find('Abstract/AbstractText')
        return abstract.text

    @property
    def authors(self) -> [str]:
        """Names of authors published with article."""
        authors: [str] = []
        author_list = self._article_element.findall('AuthorList/Author')
        for author in author_list:
            author_lastName = author.find('LastName').text
            author_foreName = author.find('ForeName').text
            authors.append(author_lastName + ', ' + author_foreName)
        return authors

    @property
    def language(self) -> str:
        """Tha language the article was published in."""
        language = self._article_element.find('Language')
        return language.text

    @property
    def chemicals(self) -> [str]:
        """One or more chemical elements."""
        chemicals: [str] = []
        chemicals_list = self._medline_element.findall('ChemicalList/Chemical')
        for chemical in chemicals_list:
            chemicals.append(chemical.text)
        return chemicals

    @property
    def mesh_list(self) -> [str]:
        """Article's suppl mesh list."""
        meshes: [str] = []
        mesh_list = self._medline_element.findall(
            'MeshHeadingList/MeshHeading')
        for mesh in mesh_list:
            descriptor = mesh.find('DescriptorName')
            meshes.append(descriptor.text)
        return meshes

    @property
    def to_dict(self):
        """Generate article model dictionary."""
        obj_dict = {}
        obj_dict['date_completed'] = str(self.date_completed)
        raise NotImplementedError
        return obj_dict
