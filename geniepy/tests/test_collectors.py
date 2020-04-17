"""Module to test collectors."""
import pytest
from geniepy.datamgmt.collectors import CtdCollector
from geniepy.errors import SchemaError
import tests.testdata as td


class TestCtdCollector:
    """PyTest collector test class."""

    collector = CtdCollector()

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

    # @pytest.mark.parametrize("payload", td.CTD_VALID_DF)
    # def test_query(self, payload):
    #     """Test queying data."""
    #     # Save the data first
    #     self.collector.save(payload)
    #     # Query data
    #     digest = payload.Digest[0]
    #     received_df = self.collector.query(searchkey=digest)
    #     # Compare data queried to payload
    #     expected_df = payload.loc[payload.Digest == digest]
    #     assert expected_df.equals(received_df)
