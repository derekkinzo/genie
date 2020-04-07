"""Test pub med article model class."""
import os
import xml.etree.ElementTree as ET
from tests import get_resources_path, get_test_output_path
from pygenie.pubmed import PubMedArticle, ArticleSetParser

SAMPLE_ARTICLE1_NAME = 'sample_article1.xml'
"""Name of sample article 1 file."""
SAMPLE_ARTICLE1_PATH = os.path.join(get_resources_path(), SAMPLE_ARTICLE1_NAME)

ARTICLE_XML: ET.Element = ET.parse(SAMPLE_ARTICLE1_PATH).getroot()
TEST_ARTICLE = PubMedArticle(ARTICLE_XML)


class TestPubMedArticle():
    """Test class for functionlities related to PubMedArticle class."""

    def test_article_constructor(self):
        """Construct pubmed article object from xml."""
        assert TEST_ARTICLE is not None

    def test_pmid(self):
        """Verify article id."""
        expected_pmid = '1'
        pmid = TEST_ARTICLE.pmid
        assert pmid == expected_pmid

    def test_date_completed(self):
        """Verify article date completed."""
        expected_date = '1976-01-16'
        date_completed = TEST_ARTICLE.date_completed
        assert date_completed == expected_date

    def test_article_pubmodel(self):
        """Verify PubModel - medium which cited article was published."""
        expected_pub_model = 'Print'
        assert TEST_ARTICLE.pub_model == expected_pub_model

    def test_title(self):
        """Verify title of journal."""
        expected_title = 'Biochemical medicine'
        title = TEST_ARTICLE.title
        assert title == expected_title

    def test_iso_abbrev(self):
        """The title ISO abbreviation."""
        expected_iso_abbrev = 'Biochem Med'
        iso_abbrev = TEST_ARTICLE.iso_abbreviation
        assert iso_abbrev == expected_iso_abbrev

    def test_article_title(self):
        """Entire title of journal article in English."""
        expected_article_title = 'Formate assay in body fluids: application in methanol poisoning.'
        article_title = TEST_ARTICLE.article_title
        assert article_title == expected_article_title

    def test_abstract(self):
        """Verify abstract of published article."""
        expected_abstract = ''
        abstract = TEST_ARTICLE.abstract
        assert abstract == expected_abstract

    def test_authors(self):
        """Verify names of authors."""
        expected_set = set(['Makar, A B',
                            'McMartin, K E',
                            'Palese, M',
                            'Tephly, T R'])
        authors_set = set(TEST_ARTICLE.authors)
        assert authors_set == expected_set

    def test_language(self):
        """Verify article language."""
        expected_language = 'eng'
        language = TEST_ARTICLE.language
        assert language == expected_language

    def test_chemical_list(self):
        """Verify list of chemicals."""
        expected_set = set(['Formates', 'Carbon Dioxide',
                            'Methanol', 'Aldehyde Oxidoreductases'])
        chemicals_set = set(TEST_ARTICLE.chemicals)
        assert chemicals_set == expected_set

    def test_mesh_list(self):
        """Verify mesh descriptors list."""
        expected_set = set(['Aldehyde Oxidoreductases',
                            'Animals',
                            'Body Fluids',
                            'Carbon Dioxide',
                            'Formates',
                            'Haplorhini',
                            'Humans',
                            'Hydrogen-Ion Concentration',
                            'Kinetics',
                            'Methanol',
                            'Methods',
                            'Pseudomonas'])
        mesh_set = set(TEST_ARTICLE.mesh_list)
        assert mesh_set == expected_set

    def test_dict(self):
        """Test object dictionary."""
        article_dict = TEST_ARTICLE.to_dict
        assert article_dict['date_completed'] == '1976-01-16'


class TestArticlesSetParser():
    """Test ArticleSetParser. i.e. xml files with array of PubMedArticles."""

    SAMPLE_ARTICLE_SET1_NAME = 'sample_articleset1.xml'
    SAMPLE_ARTICLE_SET1_PATH = os.path.join(
        get_resources_path(), SAMPLE_ARTICLE_SET1_NAME)

    def test_extract_articles(self):
        """Extract pubmed articles from article set."""
        articles: [PubMedArticle] = ArticleSetParser.extract_articles(
            self.SAMPLE_ARTICLE_SET1_PATH)
        assert articles is not None
        assert len(articles) == 2
        assert isinstance(articles[0], PubMedArticle)

    def test_articles_to_json(self):
        """Serialize pubmedarticle object into json file."""
        articles: [PubMedArticle] = ArticleSetParser.extract_articles(
            self.SAMPLE_ARTICLE_SET1_PATH)
        target_file_name = 'test_articles.json'
        target_path = os.path.join(get_test_output_path(), target_file_name)
        ArticleSetParser.articles_to_json(articles, target_path)

    def test_articles_to_jsonl(self):
        """Serialize pubmedarticles objects into jsonl file."""
        articles: [PubMedArticle] = ArticleSetParser.extract_articles(
            self.SAMPLE_ARTICLE_SET1_PATH
        )
        target_file_name = 'test_articles.jsonl'
        target_path = os.path.join(get_test_output_path(), target_file_name)
        ArticleSetParser.articles_to_jsonl(articles, target_path)

    def test_serialize_to_pipe_delimited(self):
        """Serialize pubmedarticles to csv file."""
        articles: [PubMedArticle] = ArticleSetParser.extract_articles(
            self.SAMPLE_ARTICLE_SET1_PATH)
        target_file_name = 'test_articles.csv'
        target_path = os.path.join(get_test_output_path(), target_file_name)
        ArticleSetParser.articles_to_pipe(articles, target_path)
