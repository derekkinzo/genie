# """Test Data Access Object Manager."""
# import pytest
# import geniepy.datamgmt.daos as daos
# import geniepy.datamgmt.repositories as dr
# from geniepy.datamgmt.tables import PUBMED_PROPTY, CTD_PROPTY, CLSFR_PROPTY
# from geniepy.datamgmt import DaoManager
# import tests.resources.mock as mock
# from tests.resources.mock import TEST_CHUNKSIZE


# class TestDaoManager:
#     """Pytest data access object manager test class."""

#     # Create and configure mock ctd dao
#     ctd_dao = daos.CtdDao(dr.SqlRepository("sqlite://", CTD_PROPTY))
#     # pylint: disable=protected-access
#     ctd_dao._parser.scraper = mock.MockCtdScraper()

#     # Create and configure mock pubmed dao
#     pubmed_dao = daos.PubMedDao(dr.SqlRepository("sqlite://", PUBMED_PROPTY))
#     # pylint: disable=protected-access
#     pubmed_dao._parser.scraper = mock.MockPubMedScraper()

#     # Create and configure mock classifier dao
#     classifier_dao = daos.ClassifierDao(dr.SqlRepository("sqlite://", CLSFR_PROPTY))
#     # pylint: disable=protected-access

#     # Construct mock dao manager for testing
#     dao_mgr = DaoManager(
#         ctd_dao=ctd_dao, pubmed_dao=pubmed_dao, classifier_dao=classifier_dao
#     )

#     def test_constructor(self):
#         """Test obj construction."""
#         assert self.dao_mgr is not None

#     def test_dowload_and_get_records(self):
#         """Test download and get_records functionality of DAO Mgr."""
#         gen_df = self.dao_mgr.gen_records(TEST_CHUNKSIZE)
#         # After instantiation dao's tables should be empty, so nothing is returned.
#         with pytest.raises(StopIteration):
#             next(gen_df)
#         # Call download function to scrape data and generate internal tables.
#         self.dao_mgr.download(TEST_CHUNKSIZE)
#         # Make sure gen_df is not none and conforms to expected schema
#         gen_df = self.dao_mgr.gen_records(TEST_CHUNKSIZE)
#         records = next(gen_df)
#         assert records is not None

#     @pytest.mark.parametrize("chunksize", [*range(1, 10)])
#     def test_get_records_chunksize(self, chunksize):
#         """Test get records chunksizes."""
#         self.dao_mgr.download(TEST_CHUNKSIZE)
#         gen_df = self.dao_mgr.gen_records(chunksize=chunksize)
#         records = next(gen_df)
#         # Make sure records contain correct chunk
#         assert records.shape[0] == chunksize

#     def test_save_predictions(self):
#         """Test writing predictions to output tables."""
#         self.dao_mgr.download(TEST_CHUNKSIZE)
#         gen_df = self.dao_mgr.gen_records(TEST_CHUNKSIZE)
#         records = next(gen_df)
#         predictions_df = mock.MOCK_CLSFRMGR.predict(records)
#         self.dao_mgr.save_predictions(predictions_df)
#         # Read data back from output tables to make sure records were saved
#         clsfr_dao = self.dao_mgr._classifier_dao
#         saved_df = next(clsfr_dao.query(clsfr_dao.query_all, TEST_CHUNKSIZE))
#         assert saved_df.equals(predictions_df)

# @pytest.mark.parametrize("chunksize", [*range(1, 10)])
# def test_get_records_chunksize(self, chunksize):
#     """Test get records chunksizes."""
#     self.dao_mgr.download(TEST_CHUNKSIZE)
#     gen_df = self.dao_mgr.gen_records(chunksize=chunksize)
#     records = next(gen_df)
#     # Make sure records contain correct chunk
#     assert records.shape[0] == chunksize
