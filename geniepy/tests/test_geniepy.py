"""Test high-level application calls."""
import geniepy.genie as genie


def test_run_job():
    """Test top-level cron job function."""
    genie.run_job()
    raise NotImplementedError


def test_update_tables():
    """Test scrape internet and update database."""
    genie.update_tables()
    raise NotImplementedError


def test_update_predictions():
    """Test running predictions and updating database."""
    genie.update_predictions()
    raise NotImplementedError
