"""Test Classification Manager Module."""
import pytest
from geniepy.errors import ClassifierError
import geniepy.datamgmt.daos as daos
import geniepy.datamgmt.repositories as dr
from geniepy.datamgmt.tables import PUBMED_PROPTY, CTD_PROPTY, CLSFR_PROPTY
from geniepy.datamgmt import DaoManager
from geniepy.datamgmt.parsers import ClassifierParser
from tests.resources.mock import MOCK_CLSFRMGR, TEST_CHUNKSIZE
import tests.resources.mock as mock


class TestClassMgr:
    """PyTest Class to test Classification manager."""

    # Create and configure mock ctd dao
    ctd_dao = daos.CtdDao(dr.SqlRepository("sqlite://", CTD_PROPTY))
    # pylint: disable=protected-access
    ctd_dao._parser.scraper = mock.MockCtdScraper()

    # Create and configure mock pubmed dao
    pubmed_dao = daos.PubMedDao(dr.SqlRepository("sqlite://", PUBMED_PROPTY))
    # pylint: disable=protected-access
    pubmed_dao._parser.scraper = mock.MockPubMedScraper()

    # Create and configure mock pubmed dao
    classifier_dao = daos.ClassifierDao(dr.SqlRepository("sqlite://", CLSFR_PROPTY))
    # pylint: disable=protected-access

    # Construct mock dao manager for testing
    dao_mgr = DaoManager(
        ctd_dao=ctd_dao, pubmed_dao=pubmed_dao, classifier_dao=classifier_dao
    )

    def test_constructor(self):
        """Test obj construction."""
        assert MOCK_CLSFRMGR is not None

    def test_predict_invalid_records(self):
        """Test attempting to predict with invalid records."""
        with pytest.raises(ClassifierError):
            MOCK_CLSFRMGR.predict(None)
