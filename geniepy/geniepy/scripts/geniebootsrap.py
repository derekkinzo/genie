"""
Module to bootstrap genie to scripts.

Scripts in this directory may call genie packages, this module adds genie
top-level dir to python path for scripts to be able to import genie.
"""
import sys
from pathlib import Path

GENIE_PATH = Path(__file__).resolve().parents[2]
sys.path.append(str(GENIE_PATH))
