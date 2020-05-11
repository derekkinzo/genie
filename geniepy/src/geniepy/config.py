"""
GeniePy Configuration Module.

This module is intended to provide functions that interprets content from the
package configuration file and generate the corresponding python objects.
"""
from shutil import copyfile
import yaml
from pathlib import Path
from geniepy.errors import ConfigError
import logging
import sys
from logging.handlers import TimedRotatingFileHandler

CONFIG_DIR = Path("~/.geniepy.d/").expanduser().resolve()
CONFIG_DIR.mkdir(parents=True, exist_ok=True)
TMP_DIR = CONFIG_DIR.joinpath("tmp").resolve()
TMP_DIR.mkdir(parents=True, exist_ok=True)

CONFIG_NAME = "config.yaml"
CONFIG_FILE = CONFIG_DIR.joinpath(CONFIG_NAME).resolve()
DEFAULT_CONFIG = Path(__file__).parent.joinpath(CONFIG_NAME).resolve()

LOG_FORMATTER = logging.Formatter(
    "%(asctime)s — %(name)s — %(levelname)s — %(message)s"
)
LOG_NAME = "geniepy.log"
LOG_FILE = CONFIG_DIR.joinpath(LOG_NAME)
LOG_FILE.touch()

# Check for config.yaml in geniepy dir. Otherwise, create default
if not CONFIG_FILE.exists():
    copyfile(DEFAULT_CONFIG, CONFIG_FILE)
    print(
        f"""Created default configuration. Please configure geniepy and
add your Google Big Query credentials. {str(CONFIG_FILE)}"""
    )


def read_yaml() -> dict:
    """Read yaml configuration file and return dict."""
    with open(CONFIG_FILE) as config_file:
        return yaml.load(config_file, Loader=yaml.FullLoader)


def get_model() -> str:
    """Return the model file_id."""
    configdict = read_yaml()
    return configdict["model"]


def get_projname() -> str:
    """Retrieve gbq project name from config file."""
    configdict = read_yaml()
    return configdict["gbq"]["proj"]


def get_dataset(dsname: str) -> str:
    """Retrive gbq dataset from config file. 'master' or 'scoring'."""
    configdict = read_yaml()
    return configdict["gbq"]["dataset"][dsname]


def get_chunksize() -> int:
    """Retrieve standard genie generators chunk size."""
    configdict = read_yaml()
    return configdict["chunksize"]


def get_max_workers() -> int:
    """Retrieve standard genie generators maximum parallel processes."""
    configdict = read_yaml()
    return configdict["max_workers"]


def get_credentials() -> str:
    """Get credentials file path from config."""
    configdict = read_yaml()
    credentials_file = Path(configdict["gbq"]["credentials"]).expanduser()
    credentials_path = Path.cwd().joinpath(credentials_file).resolve()
    if not credentials_path.exists():
        # TODO log error properly
        print(f"Invalid configuration file: {credentials_path}")
        raise ConfigError("Credentials path not found")
    return credentials_path


def get_pubmed_ftp_server() -> str:
    """Retrieve PubMed FTP Server."""
    configdict = read_yaml()
    return configdict["pubmed_ftp_server"]


def get_pubmed_baseline_dir() -> str:
    """Retrieve PubMed FTP Directory for Baseline Dataset."""
    configdict = read_yaml()
    return configdict["pubmed_baseline_dir"]


def get_pubmed_update_dir() -> str:
    """Retrieve PubMed FTP Directory for Update Dataset."""
    configdict = read_yaml()
    return configdict["pubmed_update_dir"]


def get_pubmed_data_file() -> str:
    """Retrieve path for PubMed data file."""
    configdict = read_yaml()
    return configdict["pubmed_data_file"]


def get_pubmed_download_dir() -> str:
    """Retrieve path where to download PubMed data files."""
    configdict = read_yaml()
    return configdict["pubmed_download_dir"]


def get_logger(logger_name: str):
    """Retrieve geniepy logger."""
    file_handler = TimedRotatingFileHandler(LOG_FILE, when="midnight")
    file_handler.setFormatter(LOG_FORMATTER)
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    logger.addHandler(logging.StreamHandler(sys.stdout))
    logger.propagate = False
    return logger
