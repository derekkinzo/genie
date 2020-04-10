"""Tests entry point module containing definition and helper functions."""

import os

RESOURCES_DIR = 'resources'
"""Name of test resources directory."""

OUTPUT_DIR = 'tests_output'
"""Name of temporary tests output directory to store test files."""


def get_resources_path() -> str:
    """Return absolute path to resources directory."""
    current_path = os.path.dirname(os.path.realpath(__file__))
    resources_path = os.path.join(current_path, RESOURCES_DIR)
    return resources_path


def gen_dir(dir_path: str):
    """Generate dir if doesn't exist."""
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)


def get_test_output_path() -> str:
    """
    Get output path to test output directory.

    The test output directory is a temporary, automatically generated,
    directory to store test output and files.

    Returns:
        str -- absolute path to test output directory
    """
    current_path = os.path.dirname(os.path.relpath(__file__))
    output_path = os.path.join(current_path, OUTPUT_DIR)
    gen_dir(output_path)
    return output_path
