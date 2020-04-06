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

    MEDLINE_TAG = 'MedlineCitation'
    ARTICLE_TAG = MEDLINE_TAG + '/Article'
    JOURNAL_TAG = ARTICLE_TAG + '/Journal'

    __slots__ = ['_pubmed_article']

    def __init__(self, article_tree: ET.Element):
        """Construct object from corresponding article element tree."""
        self._pubmed_article: ET.Element = article_tree

    def _get_xml_element(self, tags: [str], tag_attrib=None) -> str:
        """
        Retrieve xml element given full element xml path.

        Arguments:
            element [str] -- list of xml sub tags to target elmeent
                                i.e. ['MedlineCitation', 'PMID']
            tag_attib -- Optional attribute if retrieving atrrib

        Returns:
            str -- The text value of the queried element. If element doesn't
                    exist returns empty string.
        """
        element_path = ''
        for tag in tags:
            element_path += tag + '/'
        element_path = element_path[:-1]  # remove last '/'
        element = self._pubmed_article.find(element_path)
        if element is None:
            return ''

        if tag_attrib is None:
            return element.text
        else:
            return element.attrib[tag_attrib]

    @property
    def pmid(self) -> str:
        """Pubmed article ID."""
        pmid = self._get_xml_element([self.MEDLINE_TAG, 'PMID'])
        return pmid

    @property
    def date_completed(self) -> str:
        """Date completed record distributed to PubMed."""
        year = self._get_xml_element([self.MEDLINE_TAG,
                                      'DateCompleted',
                                      'Year'])
        month = self._get_xml_element([self.MEDLINE_TAG,
                                       'DateCompleted',
                                       'Month'])
        day = self._get_xml_element([self.MEDLINE_TAG,
                                     'DateCompleted',
                                     'Day'])
        return year + '-' + month + '-' + day

    @property
    def pub_model(self) -> str:
        """Publication model - medium/media in which article was published."""
        pub_model = self._get_xml_element(
            [self.ARTICLE_TAG], tag_attrib='PubModel')
        return pub_model

    @property
    def title(self) -> str:
        """Full journal title."""
        title = self._get_xml_element([self.JOURNAL_TAG, 'Title'])
        return title

    @property
    def iso_abbreviation(self) -> str:
        """Journal title ISO abbreviation."""
        iso_abbrev = self._get_xml_element(
            [self.JOURNAL_TAG, 'ISOAbbreviation'])
        return iso_abbrev

    @property
    def article_title(self) -> str:
        """Entire title of journal article in English."""
        article_title = self._get_xml_element(
            [self.ARTICLE_TAG, 'ArticleTitle'])
        return article_title

    @property
    def abstract(self) -> str:
        """Entire abstract taken directly from published article."""
        abstract = self._get_xml_element(
            [self.ARTICLE_TAG, 'Abstract', 'AbstractText'])
        return abstract

    @property
    def authors(self) -> [str]:
        """Names of authors published with article."""
        authors: [str] = []
        author_list = self._pubmed_article.findall(
            self.ARTICLE_TAG + '/AuthorList/Author')
        for author in author_list:
            author_lastname = author.find('LastName').text
            author_forename = author.find('ForeName').text
            authors.append(author_lastname + ', ' + author_forename)
        return authors

    @property
    def language(self) -> str:
        """Tha language the article was published in."""
        language = self._get_xml_element([self.ARTICLE_TAG, 'Language'])
        return language

    @property
    def chemicals(self) -> [str]:
        """One or more chemical elements."""
        chemicals: [str] = []
        chemicals_list = self._pubmed_article.findall(
            self.MEDLINE_TAG + '/ChemicalList/Chemical')
        for chemical in chemicals_list:
            chemical_substance = chemical.find('NameOfSubstance')
            if chemical_substance is not None:
                chemicals.append(chemical_substance.text)
        return chemicals

    @property
    def mesh_list(self) -> [str]:
        """Article's suppl mesh list."""
        meshes: [str] = []
        mesh_list = self._pubmed_article.findall(
            self.MEDLINE_TAG + '/MeshHeadingList/MeshHeading')
        for mesh in mesh_list:
            descriptor = mesh.find('DescriptorName')
            if descriptor is not None:
                meshes.append(descriptor.text)
        return meshes

    @property
    def to_dict(self):
        """Generate article model dictionary."""
        _dict = {}
        _dict['pmid'] = self.pmid
        _dict['date_completed'] = self.date_completed
        _dict['pub_model'] = self.pub_model
        _dict['title'] = self.title
        _dict['iso_abbreviation'] = self.iso_abbreviation
        _dict['article_title'] = self.article_title
        _dict['abstract'] = self.abstract
        _dict['authors'] = self.authors
        _dict['language'] = self.language
        _dict['chemicals'] = self.chemicals
        _dict['mesh_list'] = self.mesh_list
        return _dict
