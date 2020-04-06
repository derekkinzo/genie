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


def test_date_completed():
    """Verify article date completed."""
    expected_date = '1976-01-16'
    date_completed = str(TEST_ARTICLE.date_completed)
    assert date_completed == expected_date


def test_article_pubmodel():
    """Verify PubModel - medium which cited article was published."""
    expected_pub_model = 'Print'
    assert TEST_ARTICLE.pub_model == expected_pub_model


def test_date_pub():
    """Verify article publication date."""
    expected_date = '1975-Jun'
    date_pub = str(TEST_ARTICLE.date_pub)
    assert date_pub == expected_date


def test_title():
    """Verify title of journal."""
    expected_title = 'Biochemical medicine'
    title = TEST_ARTICLE.title
    assert title == expected_title


def test_iso_abbrev():
    """The title ISO abbreviation."""
    expected_iso_abbrev = 'Biochem Med'
    iso_abbrev = TEST_ARTICLE.iso_abbreviation
    assert iso_abbrev == expected_iso_abbrev


def test_article_title():
    """Entire title of journal article in English."""
    expected_article_title = 'Formate assay in body fluids: application in methanol poisoning.'
    article_title = TEST_ARTICLE.article_title
    assert article_title == expected_article_title


def test_abstract():
    """Verify abstract of published article."""
    expected_abstract = ''
    abstract = TEST_ARTICLE.abstract
    assert abstract == expected_abstract


def test_authors():
    """Verify names of authors."""
    expected_authors = ['Makar, A B',
                        'McMartin, K E',
                        'Palese, M',
                        'Tephly, T R']
    authors = TEST_ARTICLE.authors
    assert authors.sort() == expected_authors.sort()  # need fix this comparisson


def test_language():
    """Verify article language."""
    expected_language = 'eng'
    language = TEST_ARTICLE.language
    assert language == expected_language


def test_chemical_list():
    """Verify list of chemicals."""
    expected_chemicals = ['Formates', 'D002245', 'D000445', 'D000432']
    chemicals = TEST_ARTICLE.chemicals
    assert chemicals.sort() == expected_chemicals.sort()


def test_mesh_list():
    """Verify mesh descriptors list."""
    expected_mesh = ['Aldehyde Oxidoreductases',
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
                     'Pseudomonas']
    mesh = TEST_ARTICLE.mesh_list
    assert mesh.sort() == expected_mesh.sort()


def test_dict():
    """Test object dictionary."""
    article_dict = TEST_ARTICLE.to_dict
    assert article_dict['date_completed'] == '1976-01-16'
