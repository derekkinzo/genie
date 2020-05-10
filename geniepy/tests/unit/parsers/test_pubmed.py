"""Test pub med article model class."""
import os
import collections
import xml.etree.ElementTree as ET
import pytest
from tests import get_resources_path, get_test_output_path
from geniepy.pubmed import PubMedArticle, ArticleSetParser


def create_article(article_name: str) -> PubMedArticle:
    """Create the article object."""
    article_path = os.path.join(get_resources_path(), article_name)
    xml_element = ET.parse(article_path).getroot()
    return PubMedArticle(xml_element)


ExpectedArticle = collections.namedtuple(
    "ExpectedArticle",
    "pmid date_completed pub_model title iso_abbrev \
                        article_title abstract authors language chemicals \
                        mesh_list",
)
ActualExpected = collections.namedtuple("TestData", "article expected")
TEST_DATA = [
    ActualExpected(
        article=create_article("sample_empty_article.xml"),
        expected=ExpectedArticle(
            pmid="",
            date_completed="--",
            pub_model="",
            title="",
            iso_abbrev="",
            article_title="",
            abstract="",
            authors=[],
            language="",
            chemicals=[],
            mesh_list=[],
        ),
    ),
    ActualExpected(
        article=create_article("sample_article1.xml"),
        expected=ExpectedArticle(
            pmid="1",
            date_completed="1976-01-16",
            pub_model="Print",
            title="Biochemical medicine",
            iso_abbrev="Biochem Med",
            article_title="Formate assay in body fluids: \
application in methanol poisoning.",
            abstract="",
            authors=["Makar, A B", "McMartin, K E", "Palese, M", "Tephly, T R"],
            language="eng",
            chemicals=[
                "Formates",
                "Carbon Dioxide",
                "Methanol",
                "Aldehyde Oxidoreductases",
            ],
            mesh_list=[],
        ),
    ),
    ActualExpected(
        article=create_article("sample_article2.xml"),
        expected=ExpectedArticle(
            pmid="15299998",
            date_completed="2006-02-03",
            pub_model="Print",
            title="Medicina (Kaunas, Lithuania)",
            iso_abbrev="Medicina (Kaunas)",
            article_title="[The crop-producing power and chemical \
composition of the essential oil of the cones of hop cultivars].",
            abstract='The objective of this study was to determine \
harvest yield and essential oil composition of six hop cultivars \
("Fredos derlingieji", "Alta", "Granit", "Marynka", "Dubskij zeleniak" \
and "Aromat polessja") cultivated in Lithuania. It was found that the highest \
crop can be obtained from early and middle harvest varieties, which mature \
during the first decade of September and the third decade of August. Late \
harvest cultivars are not suitable for cultivation, however they can be used \
for the development of new cultivars. Essential oils were isolated by \
hydrodistillation and analyzed by gas chromatography and mass \
spectrometry. The highest amount of essential oil was determined \
in Marynka cultivar (2.10 ml/100 g), the lowest one in Dubskij \
zeleniak 18 (0.46 ml/100 g). Totally, 62 compounds were identified in all \
cultivars. Myrcene, beta-caryophyllene, alpha-humulene and beta-farnesene \
(E) were major constituents in the essential oils. The differences in the \
content of other essential oil constituents were determined. Some cultivars \
were rich in esters and ketones.',
            authors=["Obelevicius, Kestutis", "Venskutonis, Rimantas"],
            language="lit",
            chemicals=[
                "Monocyclic Sesquiterpenes",
                "Oils, Volatile",
                "Polycyclic Sesquiterpenes",
                "Sesquiterpenes",
                "beta-farnesene",
                "humulene",
                "caryophyllene",
            ],
            mesh_list=[
                "Chromatography, Gas",
                "Climate",
                "Humans",
                "Humulus",
                "Lithuania",
                "Mass Spectrometry",
                "Monocyclic Sesquiterpenes",
                "Oils, Volatile",
                "Polycyclic Sesquiterpenes",
                "Seasons",
                "Sesquiterpenes",
            ],
        ),
    ),
]


class TestPubMedArticle:
    """Test class for functionlities related to PubMedArticle class."""

    @pytest.mark.parametrize("data", TEST_DATA)
    def test_article_constructor(self, data):
        """Construct pubmed article object from xml."""
        assert data.article is not None

    @pytest.mark.parametrize("data", TEST_DATA)
    def test_pmid(self, data):
        """Verify article id."""
        expected_pmid = data.expected.pmid
        pmid = data.article.pmid
        assert pmid == expected_pmid

    @pytest.mark.parametrize("data", TEST_DATA)
    def test_date_completed(self, data):
        """Verify article date completed."""
        expected_date = data.expected.date_completed
        date_completed = data.article.date_completed
        assert date_completed == expected_date

    @pytest.mark.parametrize("data", TEST_DATA)
    def test_article_pubmodel(self, data):
        """Verify PubModel - medium which cited article was published."""
        expected_pub_model = data.expected.pub_model
        pub_model = data.article.pub_model
        assert pub_model == expected_pub_model

    @pytest.mark.parametrize("data", TEST_DATA)
    def test_title(self, data):
        """Verify title of journal."""
        expected_title = data.expected.title
        title = data.article.title
        assert title == expected_title

    @pytest.mark.parametrize("data", TEST_DATA)
    def test_iso_abbrev(self, data):
        """The title ISO abbreviation."""
        expected_iso_abbrev = data.expected.iso_abbrev
        iso_abbrev = data.article.iso_abbreviation
        assert iso_abbrev == expected_iso_abbrev

    @pytest.mark.parametrize("data", TEST_DATA)
    def test_article_title(self, data):
        """Entire title of journal article in English."""
        expected_article_title = data.expected.article_title
        article_title = data.article.article_title
        assert article_title == expected_article_title

    @pytest.mark.parametrize("data", TEST_DATA)
    def test_abstract(self, data):
        """Verify abstract of published article."""
        expected_abstract = data.expected.abstract
        abstract = data.article.abstract
        assert abstract == expected_abstract

    @pytest.mark.parametrize("data", TEST_DATA)
    def test_authors(self, data):
        """Verify names of authors."""
        expected_set = set(data.expected.authors)
        authors_set = set(data.article.authors)
        assert authors_set == expected_set

    @pytest.mark.parametrize("data", TEST_DATA)
    def test_language(self, data):
        """Verify article language."""
        expected_language = data.expected.language
        language = data.article.language
        assert language == expected_language

    @pytest.mark.parametrize("data", TEST_DATA)
    def test_chemical_list(self, data):
        """Verify list of chemicals."""
        expected_set = set(data.expected.chemicals)
        chemicals_set = set(data.article.chemicals)
        assert chemicals_set == expected_set

    @pytest.mark.parametrize("data", TEST_DATA)
    def test_mesh_list(self, data):
        """Verify mesh descriptors list."""
        expected_set = set(data.expected.mesh_list)
        mesh_set = set(data.article.mesh_list)
        assert mesh_set == expected_set

    @pytest.mark.parametrize("data", TEST_DATA)
    def test_dict(self, data):
        """Test object dictionary."""
        assert data.article.to_dict is not None


class TestArticlesSetParser:
    """Test ArticleSetParser. i.e. xml files with array of PubMedArticles."""

    SAMPLE_ARTICLE_SET1_NAME = "sample_articleset1.xml"
    SAMPLE_ARTICLE_SET1_PATH = os.path.join(
        get_resources_path(), SAMPLE_ARTICLE_SET1_NAME
    )

    def test_extract_articles(self):
        """Extract pubmed articles from article set."""
        articles: [PubMedArticle] = ArticleSetParser.extract_articles(
            self.SAMPLE_ARTICLE_SET1_PATH
        )
        assert articles is not None
        assert len(articles) == 2
        assert isinstance(articles[0], PubMedArticle)

    def test_articles_to_json(self):
        """Serialize pubmedarticle object into json file."""
        articles: [PubMedArticle] = ArticleSetParser.extract_articles(
            self.SAMPLE_ARTICLE_SET1_PATH
        )
        target_file_name = "test_articles.json"
        target_path = os.path.join(get_test_output_path(), target_file_name)
        ArticleSetParser.articles_to_json(articles, target_path)

    def test_articles_to_jsonl(self):
        """Serialize pubmedarticles objects into jsonl file."""
        articles: [PubMedArticle] = ArticleSetParser.extract_articles(
            self.SAMPLE_ARTICLE_SET1_PATH
        )
        target_file_name = "test_articles.jsonl"
        target_path = os.path.join(get_test_output_path(), target_file_name)
        ArticleSetParser.articles_to_jsonl(articles, target_path)

    def test_serialize_to_pipe_delimited(self):
        """Serialize pubmedarticles to csv file."""
        articles: [PubMedArticle] = ArticleSetParser.extract_articles(
            self.SAMPLE_ARTICLE_SET1_PATH
        )
        target_file_name = "test_articles.csv"
        target_path = os.path.join(get_test_output_path(), target_file_name)
        ArticleSetParser.articles_to_pipe(articles, target_path)
