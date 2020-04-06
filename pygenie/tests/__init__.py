"""Tests entry point module containing definition and helper functions."""

import os

RESOURCES_DIR = 'resources'
"""Name of test resources directory."""


def get_resources_path() -> str:
    """Return absolute path to resources directory."""
    current_path = os.path.dirname(os.path.realpath(__file__))
    resources_path = os.path.join(current_path, RESOURCES_DIR)
    return resources_path
