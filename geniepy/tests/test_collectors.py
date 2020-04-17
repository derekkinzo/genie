"""Module to test collectors."""
import pytest
import pandas as pd
from typing import Generator
from geniepy.datamgmt.collectors import CtdCollector
from geniepy.errors import SchemaError
import tests.testdata as td
from geniepy.errors import DaoError
import geniepy.datamgmt.daorepositories as dr


class TestCtdCollector:
    """PyTest collector test class."""

    collector = CtdCollector(
        dr.SqlDaoRepo("sqlite://", dr.CTD_TABLE_NAME, dr.CTD_DAO_SCHEMA)
    )

    def read_table(self, chunksize=dr.CHUNKSIZE) -> Generator[pd.DataFrame, None, None]:
        """Read entire database table (tests helper method)."""
        query_str = f"SELECT * FROM {self.collector.tablename};"
        generator = self.collector.query(query=query_str, chunksize=chunksize)
        return generator

    def read_record(self, digest):
        """Read record(s) from database (tests helper method)."""
        query_str = f"SELECT * FROM {self.collector.tablename} WHERE Digest='{digest}';"
        generator = self.collector.query(query=query_str)
        return generator

    def test_constructor(self):
        """Ensure scraper obj constructed successfully."""
        assert self.collector is not None

    @pytest.mark.parametrize("payload", td.CTD_INVALID_DF)
    def test_save_invalid_df(self, payload):
        """Test save invalid dataframe to collector's DAO."""
        with pytest.raises(SchemaError):
            self.collector.save(payload)

    @pytest.mark.parametrize("payload", td.CTD_VALID_DF)
    def test_save_valid_df(self, payload):
        """Test save valid dataframe to collector's DAO doesn't raise error."""
        self.collector.save(payload)

    @pytest.mark.parametrize("payload", td.CTD_VALID_DF)
    def test_query(self, payload):
        """Query valid record."""
        # Try to create records in db for test if don't exist
        try:
            self.collector.save(payload)
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

    @pytest.mark.parametrize("chunksize", [*range(1, len(td.CTD_VALID_DF) + 1)])
    def test_generator_chunk(self, chunksize):
        """Query all by chunk."""
        # Try to fill database, in case is empty
        for record in td.CTD_VALID_DF:
            try:
                self.collector.save(record)
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
        # Make sure collector's database is empty
        generator = self.read_table()
        with pytest.raises(StopIteration):
            # Generator should not return anything since database should be empty
            next(generator)
        # Call download method to update database with data from online sources
        self.collector.download()
        # Check new data available in database
        generator = self.read_table()
        # Generator should return values
        result_df = next(generator)
        assert result_df.Digest.count() > 0
