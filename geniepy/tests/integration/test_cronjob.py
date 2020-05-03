"""Test cron job functionalities."""
import pytest
import geniepy


@pytest.mark.slow_integration_test
def test_update_sjr():
    """Update dao table."""
    geniepy.update_sjr()


@pytest.mark.slow_integration_test
def test_update_disease2pubtator():
    """Update dao table."""
    geniepy.update_disease2pubtator()


@pytest.mark.slow_integration_test
def test_update_tables():
    """Update all tables."""
    geniepy.update_tables()


@pytest.mark.slow_integration_test
def test_run_predictions():
    """Test calculating predictions."""
    geniepy.run_predictions()


@pytest.mark.slow_integration_test
def test_run_job():
    """Test end-to-end run cron job function."""
    geniepy.run_job()
