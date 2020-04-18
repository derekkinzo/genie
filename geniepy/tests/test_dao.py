"""Module to test Data Access Objects."""
import pytest
import pandas as pd
from typing import Generator
from geniepy.datamgmt.dao import BaseDao, CtdDao
from geniepy.errors import SchemaError
import tests.testdata as td
from tests.resources.mock import MockCtdScraper
import geniepy
from geniepy.errors import DaoError
import geniepy.datamgmt.repository as dr
from geniepy.datamgmt.parsers import CtdParser


class TestCtdDao:
    """PyTest data access object test class."""

    test_repo = dr.SqlRepository("sqlite://", dr.CTD_TABLE_NAME, dr.CTD_DAO_TABLE)
    test_dao: BaseDao = CtdDao(test_repo)
    # Attach mock scraper to parser for testing
    CtdParser.scraper = MockCtdScraper()

    def read_table(
        self, chunksize=geniepy.CHUNKSIZE
    ) -> Generator[pd.DataFrame, None, None]:
        """Read entire database table (tests helper method)."""
        query_str = f"SELECT * FROM {self.test_dao.tablename};"
        generator = self.test_dao.query(query=query_str, chunksize=chunksize)
        return generator

    def read_record(self, digest):
        """Read record(s) from database (tests helper method)."""
        query_str = f"SELECT * FROM {self.test_dao.tablename} WHERE Digest='{digest}';"
        generator = self.test_dao.query(query=query_str)
        return generator

    def test_constructor(self):
        """Ensure scraper obj constructed successfully."""
        assert self.test_dao is not None

    @pytest.mark.parametrize("payload", td.CTD_INVALID_DF)
    def test_save_invalid_df(self, payload):
        """Test save invalid dataframe to dao's repository."""
        with pytest.raises(SchemaError):
            self.test_dao.save(payload)

    @pytest.mark.parametrize("payload", td.CTD_VALID_DF)
    def test_save_valid_df(self, payload):
        """Test save valid dataframe to dao's repo doesn't raise error."""
        self.test_dao.save(payload)

    @pytest.mark.parametrize("payload", td.CTD_VALID_DF)
    def test_query(self, payload):
        """Query valid record."""
        # Try to create records in db for test if don't exist
        try:
            self.test_dao.save(payload)
        except DaoError:
            pass
        # Attempt to retrieve record
        digest = payload.Digest[0]
        generator = self.read_record(digest)
        chunk = next(generator)
        assert chunk.equals(payload)

    def test_query_non_existent(self):
        """Query non-existent record should return empty."""
        # Attempt to retrieve record
        digest = "INVALID DIGEST"
        generator = self.read_record(digest)
        # Make sure generator doesn't return anything since no records in database
        with pytest.raises(StopIteration):
            next(generator)

    def test_purge(self):
        """Test delete all records from repository."""
        # Try to fill database, in case is empty
        for record in td.CTD_VALID_DF:
            try:
                self.test_dao.save(record)
            except DaoError:
                pass
        # Delete all records
        self.test_dao.purge()
        # Make sure no records left
        generator = self.read_table()
        # generator shouldn't return anything since no records in database
        with pytest.raises(StopIteration):
            next(generator)
        # Test building and reading from table again, make sure still functional
        self.test_query(td.CTD_VALID_DF[0])

    @pytest.mark.parametrize("chunksize", [*range(1, len(td.CTD_VALID_DF) + 1)])
    def test_generator_chunk(self, chunksize):
        """Query all by chunk."""
        # Try to fill database, in case is empty
        for record in td.CTD_VALID_DF:
            try:
                self.test_dao.save(record)
            except DaoError:
                pass
        # Get all records in database
        generator = self.read_table(chunksize)
        # Make sure number generator provides df of chunksize each iteration
        result_df = next(generator)
        assert result_df.Digest.count() == chunksize

    def test_download_historical(self):
        """
        Test download method for historical data.

        The first time update is called (databases are still empty), it should download
        all historical info from online sources.
        """
        # Make sure dao's database is empty
        self.test_dao.purge()
        generator = self.read_table()
        # Generator should not return anything since database should be empty
        with pytest.raises(StopIteration):
            next(generator)
        # Call download method to update database with data from online sources
        self.test_dao.chunksize = 3
        self.test_dao.download()
        # Check new data available in database
        generator = self.read_table()
        # Generator should return values
        result_df = next(generator)
        assert not result_df.empty
        # Rever chunk size so don't affect other tests
        self.test_dao.chunksize = geniepy.CHUNKSIZE
