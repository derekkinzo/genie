"""Pytest module to test Google BigQuery Repository."""
import pandas as pd
from google.oauth2 import service_account
import pandas_gbq
import geniepy.datamgmt.repositories as dr

credentials_path = ""
project_name = ""
table_name = "test." + dr.PUBMED_TABLE_NAME


class TestGbqRepository:
    """Test db repository on Google BigQuery."""

    repo: dr.BaseRepository = dr.GbqRepository(
        project_name, table_name, dr.PUBMED_DAO_TABLE, credentials_path
    )

    def test_constructor(self):
        """Test constructing object."""
        assert self.repo is not None
