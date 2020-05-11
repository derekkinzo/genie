"""PubMed related functionality."""
import xml.etree.ElementTree as ET
import json
import csv
import jsonlines


class PubMedArticle:
    """
    PubMed Article model.

    Reference documentation:
    https: // www.nlm.nih.gov/bsd/licensee/elements_descriptions.html
    """

    MEDLINE_TAG = "MedlineCitation"
    ARTICLE_TAG = MEDLINE_TAG + "/Article"
    JOURNAL_TAG = ARTICLE_TAG + "/Journal"

    __slots__ = ["_pubmed_article", "citationCount", "citationPmid"]

    def __init__(self, article_tree: ET.Element):
        """Construct object from corresponding article element tree."""
        self._pubmed_article: ET.Element = article_tree
        self.citationCount: int = 0
        self.citationPmid: str = ""

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
        element_path = ""
        for tag in tags:
            element_path += tag + "/"
        element_path = element_path[:-1]  # remove last '/'
        element = self._pubmed_article.find(element_path)
        if element is None:
            return ""

        if tag_attrib is None:
            return element.text
        else:
            return element.attrib[tag_attrib]

    @property
    def pmid(self) -> str:
        """Pubmed article ID."""
        pmid = self._get_xml_element([self.MEDLINE_TAG, "PMID"])
        return pmid

    @property
    def date_completed(self) -> str:
        """Date completed record distributed to PubMed."""
        year = self._get_xml_element([self.MEDLINE_TAG, "DateCompleted", "Year"])
        month = self._get_xml_element([self.MEDLINE_TAG, "DateCompleted", "Month"])
        day = self._get_xml_element([self.MEDLINE_TAG, "DateCompleted", "Day"])
        return year + "-" + month + "-" + day

    @property
    def pub_model(self) -> str:
        """Publication model - medium/media in which article was published."""
        pub_model = self._get_xml_element([self.ARTICLE_TAG], tag_attrib="PubModel")
        return pub_model

    @property
    def title(self) -> str:
        """Full journal title."""
        title = self._get_xml_element([self.JOURNAL_TAG, "Title"])
        return title

    @property
    def iso_abbreviation(self) -> str:
        """Journal title ISO abbreviation."""
        iso_abbrev = self._get_xml_element([self.JOURNAL_TAG, "ISOAbbreviation"])
        return iso_abbrev

    @property
    def article_title(self) -> str:
        """Entire title of journal article in English."""
        article_title = self._get_xml_element([self.ARTICLE_TAG, "ArticleTitle"])
        return article_title

    @property
    def abstract(self) -> str:
        """Entire abstract taken directly from published article."""
        abstract = self._get_xml_element([self.ARTICLE_TAG, "Abstract", "AbstractText"])
        return abstract

    @property
    def authors(self) -> [str]:
        """Names of authors published with article."""
        authors: [str] = []
        author_list = self._pubmed_article.findall(
            self.ARTICLE_TAG + "/AuthorList/Author"
        )
        for author in author_list:
            lastname_el = author.find("LastName")
            author_lastname = "" if lastname_el is None else lastname_el.text

            forename_el = author.find("ForeName")
            author_forename = "" if forename_el is None else forename_el.text

            authors.append(author_lastname + ", " + author_forename)
        return authors

    @property
    def language(self) -> str:
        """Tha language the article was published in."""
        language = self._get_xml_element([self.ARTICLE_TAG, "Language"])
        return language

    @property
    def chemicals(self) -> [str]:
        """One or more chemical elements."""
        chemicals: [str] = []
        chemicals_list = self._pubmed_article.findall(
            self.MEDLINE_TAG + "/ChemicalList/Chemical"
        )
        for chemical in chemicals_list:
            chemical_substance = chemical.find("NameOfSubstance")
            if chemical_substance is not None:
                chemicals.append(chemical_substance.text)
        return chemicals

    @property
    def mesh_list(self) -> [str]:
        """Article's suppl mesh list."""
        meshes: [str] = []
        mesh_list = self._pubmed_article.findall(
            self.MEDLINE_TAG + "/MeshHeadingList/MeshHeading"
        )
        for mesh in mesh_list:
            descriptor = mesh.find("DescriptorName")
            if descriptor is not None:
                meshes.append(descriptor.text)
        return meshes

    @property
    def issn(self) -> str:
        """Journal ISSN ID."""
        issn = self._get_xml_element([self.JOURNAL_TAG, "ISSN"])
        return issn

    @property
    def issn_type(self) -> str:
        """Journal ISSN Type."""
        issn_type = self._get_xml_element(
            [self.JOURNAL_TAG, "ISSN"], tag_attrib="IssnType"
        )
        return issn_type

    @property
    def citation_count(self) -> str:
        """Journal ISSN Type."""
        issn_type = self._get_xml_element(
            [self.JOURNAL_TAG, "ISSN"], tag_attrib="IssnType"
        )
        return issn_type

    def set_citationCount(self, citation_count: int):
        """Update property: citation_count."""
        self.citationCount = citation_count

    def set_citationPmid(self, citation_pmid: str):
        """Update property: citation_pmid."""
        self.citationPmid = citation_pmid

    @property
    def to_dict(self):
        """Generate article model dictionary."""
        _dict = {}
        _dict["pmid"] = self.pmid
        _dict["date_completed"] = self.date_completed
        _dict["pub_model"] = self.pub_model
        _dict["title"] = self.title
        _dict["iso_abbreviation"] = self.iso_abbreviation
        _dict["article_title"] = self.article_title
        _dict["abstract"] = self.abstract
        _dict["authors"] = self.authors
        _dict["language"] = self.language
        _dict["chemicals"] = self.chemicals
        _dict["mesh_list"] = self.mesh_list
        _dict["issn"] = self.issn
        _dict["issn_type"] = self.issn_type
        _dict["citation_count"] = self.citationCount
        _dict["citation_pmid"] = self.citationPmid
        return _dict


class ArticleSetParser:
    """
    Parsing utility for PubMed Article sets.

    An article set is an xml file with an array of <PubMedArticles>.
    """

    @staticmethod
    def extract_articles(xml_file_path: str) -> [PubMedArticle]:
        """
        Extract articles from xml file.

        Arguments:
            xml_file_path {str} -- absolute path to xml file

        Returns:
            [PubMedArticle] -- List of pubmed article objects
        """
        xml_root: ET.Element = ET.parse(xml_file_path).getroot()
        articles_xml_list = xml_root.findall("PubmedArticle")
        pubmed_articles: [PubMedArticle] = []
        for article_xml in articles_xml_list:
            pubmed_articles.append(PubMedArticle(article_xml))
        return pubmed_articles

    @staticmethod
    def articles_to_dict(articles: [PubMedArticle]) -> [dict]:
        """Generate list of dictionaries from articles."""
        dict_list = []
        for article in articles:
            dict_list.append(article.to_dict)
        return dict_list

    @staticmethod
    def articles_to_json(articles: [PubMedArticle], target_file_path: str):
        """Serialize pubmedarticle objects to json file."""
        dict_list = ArticleSetParser.articles_to_dict(articles)
        articles_json = json.dumps({"articles": dict_list})
        with open(target_file_path, "w") as target_file:
            target_file.write(articles_json)

    @staticmethod
    def articles_to_jsonl(articles: [PubMedArticle], target_file_path: str):
        """Serialize pubmedarticle objects to jsonl file."""
        dict_list = ArticleSetParser.articles_to_dict(articles)
        with jsonlines.open(target_file_path, "w") as writer:
            # pylint: disable=E1101
            writer.write_all(dict_list)

    @staticmethod
    def articles_to_pipe(articles: [PubMedArticle], target_file_path: str):
        """Serialize pubmedarticle objects to csv file."""
        dict_list = ArticleSetParser.articles_to_dict(articles)
        csv_columns = [
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

        try:
            with open(target_file_path, "w", encoding="utf-8") as csv_file:
                writer = csv.DictWriter(csv_file, delimiter="|", fieldnames=csv_columns)
                writer.writeheader()
                for article in dict_list:
                    writer.writerow(article)
        except IOError:  # pragma: no cover
            print("Unable to write csv file")
