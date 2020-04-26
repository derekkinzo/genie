"""Module containing helper functions for running genie scripts."""
import gzip
import shutil


def decompress_gz(file_path: str, output_file: str):
    """
    Unzip articles sets and create xml file.

    Arguments:
        file_path {str} -- absolute path gz file
        output_file {str} -- absolute path to created decompressed file
    """
    with gzip.open(file_path, "rb") as f_in:
        with open(output_file, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)
