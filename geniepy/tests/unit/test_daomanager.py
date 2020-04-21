"""Test Data Access Object Manager."""
from typing import Generator
from geniepy.datamgmt import DaoManager


class TestDaoManager:
    """Pytest data access object manager test class."""

    dao_mgr = DaoManager()

    def test_constructor(self):
        """Test obj construction."""
        assert self.dao_mgr is not None

    def test_gen_records(self):
        """Test gen_records with empty databases."""
        gen_df = self.dao_mgr.gen_records()
        assert gen_df is None
