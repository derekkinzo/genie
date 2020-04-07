"""Handle pubmed historical data. Parse and update database."""
import sys
import os
import gzip
import shutil
from pubmed import PubMedArticle, ArticleSetParser


def unzip_article_set(file_path: str, output_file: str):
    """Unzip articles sets and create xml file."""
    with gzip.open(file_path, 'rb') as f_in:
        with open(output_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)


def parse_pubmed_baseline(in_dir: str, out_dir: str):
    """Convert xml to json articles."""
    for filename in os.listdir(in_dir):
        if not filename.endswith('.gz'):
            continue
        in_file = os.path.join(in_dir, filename)
        xml_file = os.path.join(out_dir, filename.replace('.gz', ''))
        if not os.path.exists(xml_file):
            unzip_article_set(in_file, xml_file)

        article_list: PubMedArticle = ArticleSetParser.extract_articles(
            xml_file)

        output_file = xml_file.replace('.xml', '.pipe')
        ArticleSetParser.articles_to_pipe(article_list, output_file)


if __name__ == "__main__":
    ERROR_MSG = "Command line arguments expected: <path to data dir>, \
        <path to output dir>, <number of parallel processes (2-16)>"

    if not sys.argv or len(sys.argv) < 4:
        raise Exception(ERROR_MSG)

    # check command line argument for input directory
    if os.path.isdir(sys.argv[1]):
        DATA_IN_DIR = sys.argv[1]
    else:
        raise Exception("Input data directory is not valid. " + ERROR_MSG)

    # check command line argument for output directory
    if os.path.isdir(sys.argv[2]):
        DATA_OUT_DIR = sys.argv[2]
    else:
        raise Exception("Output data directory is not valid. " + ERROR_MSG)

    parse_pubmed_baseline(DATA_IN_DIR, DATA_OUT_DIR)
