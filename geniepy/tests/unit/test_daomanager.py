"""Test Data Access Object Manager."""
import geniepy.datamgmt.daos as daos
import geniepy.datamgmt.repositories as dr
from geniepy.datamgmt import DaoManager
import tests.resources.mock as mock


class TestDaoManager:
    """Pytest data access object manager test class."""

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

    # Construct mock dao manager for testing
    dao_mgr = DaoManager(ctd_dao=ctd_dao, pubmed_dao=pubmed_dao)

    def test_constructor(self):
        """Test obj construction."""
        assert self.dao_mgr is not None

    def test_dowload_and_get_records(self):
        """Test download and get_records functionality of DAO Mgr."""
        gen_df = self.dao_mgr.gen_records()
        # After instantiation dao's tables should be empty, so nothing is returned.
        assert gen_df is None
        # Call download function to scrape data and generate internal tables.
        self.dao_mgr.download()
        # Make sure gen_df is not none and conforms to expected schema
        gen_df = self.dao_mgr.gen_records()
        assert gen_df is not None
        records = next(gen_df)
        assert records is not None
