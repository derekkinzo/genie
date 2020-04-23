"""Test Classification Manager Module."""
from typing import Generator
from geniepy.classmgmt import ClassificationMgr

# from geniepy.classmgmt.classifiers import PcpClassifier
import geniepy.datamgmt.daos as daos
import geniepy.datamgmt.repositories as dr
import tests.resources.mock as mock
from geniepy.datamgmt import DaoManager
from geniepy.datamgmt.parsers import ClassifierParser


class TestClassMgr:
    """PyTest Class to test Classification manager."""

    # Create and configure mock ctd dao
    ctd_dao = daos.CtdDao(
        dr.SqlRepository("sqlite://", dr.CTD_TABLE_NAME, dr.CTD_DAO_TABLE)
    )
    # pylint: disable=protected-access
    ctd_dao._parser.scraper = mock.MockCtdScraper()

    # Create and configure mock pubmed dao
    pubmed_dao = daos.PubMedDao(
        dr.SqlRepository("sqlite://", dr.PUBMED_TABLE_NAME, dr.PUBMED_DAO_TABLE)
    )
    # pylint: disable=protected-access
    pubmed_dao._parser.scraper = mock.MockPubMedScraper()

    # Create and configure mock pubmed dao
    classifier_dao = daos.PubMedDao(
        dr.SqlRepository("sqlite://", dr.PUBMED_TABLE_NAME, dr.PUBMED_DAO_TABLE)
    )
    # pylint: disable=protected-access
    # pubmed_dao._parser.scraper = mock.MockPubMedScraper()

    # Construct mock dao manager for testing
    daomgr = DaoManager(
        ctd_dao=ctd_dao, pubmed_dao=pubmed_dao, classifier_dao=classifier_dao
    )

    classmgr: ClassificationMgr = ClassificationMgr(None)

    def test_constructor(self):
        """Test obj construction."""
        assert self.classmgr is not None

    def test_predict_records(self):
        """
        Test prediction of records.

        Records are fed into the classifier to be predicted and classification manager
        returns a dataframe containing the corresponding predictions.
        """
        # Generate records to be fed into classifiers
        self.dao_mgr.download()
        gen_df = self.dao_mgr.gen_records()
        raw_df = next(gen_df)
        predicted_df = self.classmgr.predict(raw_df)
        # Make sure predicted all rows
        expected_rows = raw_df.shape()[1]
        actual_rows = predicted_df.shape()[1]
        assert actual_rows == expected_rows
        # Make sure predicted df is valid (should return no errors)
        assert not ClassifierParser.validate(predicted_df)
        # Make sure one prediction per classifier
        cols = predicted_df.columns
        # Make sure has a digest column
        assert "digest" in cols
        num_cols = len(cols)
        # Make sure has one prediction column per classifier
        for classifier in self.classmgr._classifiers:
            assert classifier.name in cols
