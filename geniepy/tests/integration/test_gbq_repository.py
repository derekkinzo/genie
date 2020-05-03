# """Pytest module to test Google BigQuery Repository."""
# import os
# import pytest
# import tests.testdata as td
# import geniepy.datamgmt.repositories as dr
# from geniepy.datamgmt.tables import PUBMED_PROPTY, CTD_PROPTY, CLSFR_PROPTY
# from geniepy.errors import DaoError
# from tests import get_test_output_path
# from tests.resources.mock import TEST_CHUNKSIZE


# # Name of credential file (assumed to be in tests/tests_output dir)
# CREDENTIALS_FILE = "genie_credentials.json"
# CREDPATH = os.path.join(get_test_output_path(), CREDENTIALS_FILE)
# # Google BigQuery Project Name
# PROJNAME = "genie-275215"
# DATASET = "test"


# VALID_DF = td.PUBMED_VALID_DF
# INVALID_SCHEMA = td.PUBMED_INVALID_SCHEMA


# @pytest.mark.slow_integration_test
# class TestGbqRepository:
#     """Test db.pubmed_repository on Google BigQuery."""

#     pubmed_repo: dr.BaseRepository = None
#     ctd_repo: dr.BaseRepository = None
#     clsfr_repo: dr.BaseRepository = None

#     @classmethod
#     def setup_class(cls):
#         """Initialize GBQ.pubmed_repo."""
#         cls.pubmed_repo = dr.GbqRepository(PROJNAME, PUBMED_PROPTY, DATASET, CREDPATH)
#         cls.ctd_repo = dr.GbqRepository(PROJNAME, CTD_PROPTY, DATASET, CREDPATH)
#         cls.clsfr_repo = dr.GbqRepository(PROJNAME, CLSFR_PROPTY, DATASET, CREDPATH)

#     def test_constructor(self):
#         """Test constructing object."""
#         assert self.pubmed_repo is not None

#     @pytest.mark.parametrize("payload", INVALID_SCHEMA)
#     def test_save_invalid_df(self, payload):
#         """Test save invalid dataframe to dao's DAO."""
#         with pytest.raises(DaoError):
#             self.pubmed_repo.save(payload)

#     @pytest.mark.parametrize("payload", VALID_DF)
#     def test_save_valid_df(self, payload):
#         """Attempt to save dataframe with valid schema."""
#         self.pubmed_repo.save(payload)  # Don't expect to return anything

#     def test_pubmed_query(self):
#         """Query valid record."""
#         payload = VALID_DF[0]
#         # Start with empty table
#         self.pubmed_repo.delete_all()
#         # Try to create records in db for test if don't exist
#         try:
#             self.pubmed_repo.save(payload)
#         except DaoError:
#             pass
#         # Attempt to retrieve record
#         pmid = payload.pmid[0]
#         query_str = self.pubmed_repo.query_pkey(pmid)
#         generator = self.pubmed_repo.query(query_str, TEST_CHUNKSIZE)
#         chunk = next(generator)
#         assert chunk.pmid.equals(payload.pmid)

#     def test_ctd_query(self):
#         """Query valid record."""
#         payload = td.CTD_VALID_DF[0]
#         # Start with empty table
#         self.ctd_repo.delete_all()
#         # Try to create records in db for test if don't exist
#         try:
#             self.ctd_repo.save(payload)
#         except DaoError:
#             pass
#         # Attempt to retrieve record
#         digest = payload.digest[0]
#         query_str = self.ctd_repo.query_pkey(digest)
#         generator = self.ctd_repo.query(query_str, TEST_CHUNKSIZE)
#         chunk = next(generator)
#         assert chunk.digest.equals(payload.digest)

#     def test_clsfr_query(self):
#         """Query valid record."""
#         payload = td.CLSFR_VALID_DF[0]
#         # Start with empty table
#         self.clsfr_repo.delete_all()
#         # Try to create records in db for test if don't exist
#         try:
#             self.clsfr_repo.save(payload)
#         except DaoError:
#             pass
#         # Attempt to retrieve record
#         digest = payload.digest[0]
#         query_str = self.clsfr_repo.query_pkey(digest)
#         generator = self.clsfr_repo.query(query_str, TEST_CHUNKSIZE)
#         chunk = next(generator)
#         assert chunk.digest.equals(payload.digest)

#     def test_invalid_query(self):
#         """Test making invalid queries."""
#         query_str = "Invalid"
#         with pytest.raises(DaoError):
#             next(self.pubmed_repo.query(query_str, TEST_CHUNKSIZE))

#     def test_query_non_existent(self):
#         """Query non-existent record should return empty."""
#         # Attempt to retrieve record
#         pmid = 0
#         query_str = self.pubmed_repo.query_pkey(pmid)
#         generator = self.pubmed_repo.query(query_str, TEST_CHUNKSIZE)
#         # Make sure generator doesn't return anything since no matching records
#         with pytest.raises(StopIteration):
#             next(generator)

#     @pytest.mark.parametrize("chunksize", [1, 2, 3])
#     def test_generator_chunk(self, chunksize):
#         """Query all by chunk."""
#         # Start with empty table
#         self.pubmed_repo.delete_all()
#         # Try to fill database, in case is empty
#         for record in VALID_DF:
#             try:
#                 self.pubmed_repo.save(record)
#             except DaoError:
#                 pass
#         # Get all records in database
#         query_all = self.pubmed_repo.query_all
#         generator = self.pubmed_repo.query(query_all, chunksize)
#         # Make sure number generator provides df of chunksize each iteration
#         result_df = next(generator)
#         assert result_df.pmid.count() == chunksize

#     def test_delete_all(self):
#         """Test delete all records from.pubmed_repository."""
#         # Try to fill database, in case is empty
#         for record in VALID_DF:
#             try:
#                 self.pubmed_repo.save(record)
#             except DaoError:
#                 pass
#         # Delete all records
#         self.pubmed_repo.delete_all()
#         # Make sure no records left
#         query_all = self.pubmed_repo.query_all
#         generator = self.pubmed_repo.query(query_all, TEST_CHUNKSIZE)
#         # generator shouldn't return anything since no records in database
#         with pytest.raises(StopIteration):
#             next(generator)
#         # Test saving and reading from table again, make sure still functional
#         self.pubmed_repo.save(VALID_DF[0])
#         generator = self.pubmed_repo.query(query_all, TEST_CHUNKSIZE)
#         # Generator should return value
#         next(generator)
