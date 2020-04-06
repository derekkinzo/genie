"""Test pub med article model class."""
import os
import xml.etree.ElementTree as ET
from tests import get_resources_path
from pygenie.pubmed import PubMedArticle

SAMPLE_ARTICLE1_NAME = 'sample_article1.xml'
"""Name of sample article 1 file."""
SAMPLE_ARTICLE1_PATH = os.path.join(get_resources_path(), SAMPLE_ARTICLE1_NAME)

ARTICLE_XML: ET.Element = ET.parse(SAMPLE_ARTICLE1_PATH).getroot()
TEST_ARTICLE = PubMedArticle(ARTICLE_XML)


def test_article_constructor():
    """Construct pubmed article object from xml."""
    assert TEST_ARTICLE is not None


def test_medline_citation():
    """Verify Medline citation available."""
    assert TEST_ARTICLE.medline_citation is not None


def test_article_date():
    """Verify article date completed."""
    date_completed = str(TEST_ARTICLE.date_completed)
    assert date_completed == '1976-01-16'
