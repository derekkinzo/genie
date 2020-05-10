"""Test cron job functionalities."""
import pytest
import geniepy


@pytest.mark.slow_integration_test
class TestCronJob:
    """Test end-to-end functionalities."""

    def test_update_sjr(self):
        """Update dao table."""
        geniepy.update_sjr()

    def test_update_disease2pubtator(self):
        """Update dao table."""
        geniepy.update_disease2pubtator()

    def test_create_tables(self):
        """Update all tables."""
        geniepy.create_tables()

    def test_update_tables(self):
        """Update all tables."""
        geniepy.update_tables()

    def test_run_predictions(self):
        """Test calculating predictions."""
        geniepy.run_predictions()

    def test_sample(self):
        """Update all tables."""
        geniepy.sample_run()

    def test_run(self):
        """Test end-to-end run cron job function."""
        geniepy.run()
