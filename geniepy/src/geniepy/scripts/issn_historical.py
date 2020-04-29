"""
Module to extract ISSN metadata for
all available PubMed articles.
"""

from concurrent.futures import ProcessPoolExecutor
from datetime import datetime
import glob
import gzip
import os
import sys
import xml.etree.ElementTree as ET

# Constants
EXTENSION = "gz"
TAG_Article = "PubmedArticle"
TAG_PMID = "./MedlineCitation/PMID"
TAG_ISSN = "./MedlineCitation/Article/Journal/ISSN"
ATT_ISSN_TYPE = "IssnType"
_CSV_SEPRATOR = ","


def decompress_archive(file):
    with gzip.open(file, "rb") as f:
        return f.read()


def task(file):
    file_content = decompress_archive(file)
    xmlDoc = ET.fromstring(file_content)

    # get all articles
    articles = xmlDoc.findall(TAG_Article)
    if articles is None:
        return None

    # extract PMID & ISSN data
    data = []
    for article in articles:
        pmid = ""
        issn = ""
        issn_type = ""

        if not article.find(TAG_PMID) is None:
            pmid = article.find(TAG_PMID).text

        if not article.find(TAG_ISSN) is None:
            issn = article.find(TAG_ISSN).text.replace("-", "")
            issn_type = article.find(TAG_ISSN).get(ATT_ISSN_TYPE)

        if len(pmid) > 0 and len(issn) > 0:
            data.append([pmid, issn, issn_type])

    print(f"Processed data file: {os.path.basename(file)}, articles: {len(data)}")
    return data


def main(inDir, outDir, maxWorkers):
    # get list of pubmed data files
    file_path = os.path.join(inDir, f"*.{EXTENSION}")
    files = glob.glob(file_path)

    if not files or len(files) <= 0:
        return

    # start parallel processing
    start_time = datetime.now()
    with ProcessPoolExecutor(max_workers=maxWorkers) as executor:
        result = executor.map(task, files)

    # write results to csv file
    for value in result:
        out_file = f"out-issn-{datetime.now().microsecond}.csv"
        out_path = os.path.join(outDir, out_file)
        with open(out_path, "w") as file:
            file.write(
                "article_id"
                + _CSV_SEPRATOR
                + "issn_id"
                + _CSV_SEPRATOR
                + "issn_type"
                + "\n"
            )
            for article in value:
                file.write(
                    str(article[0])
                    + _CSV_SEPRATOR
                    + str(article[1])
                    + _CSV_SEPRATOR
                    + str(article[2])
                    + "\n"
                )

    tot_time = datetime.now() - start_time
    print(
        f"Processed {len(files)} PubMed data files in \
{round(tot_time.total_seconds()/60,2)} minutes"
    )


if __name__ == "__main__":
    _in_dir = ""
    _out_dir = ""
    _max_workers = ""

    ERROR_MSG = "Command line arguments expected: <path to data dir>, \
        <path to output dir>, <number of parallel processes (2-16)>"

    if not sys.argv or len(sys.argv) < 4:
        raise ValueError(ERROR_MSG)

    # check command line argument for input directory
    if os.path.isdir(sys.argv[1]):
        _in_dir = sys.argv[1]
    else:
        raise ValueError(f"Input data directory is not valid. {ERROR_MSG}")

    # check command line argument for output directory
    if os.path.isdir(sys.argv[2]):
        _out_dir = sys.argv[2]
    else:
        raise ValueError(f"Output data directory is not valid. {ERROR_MSG}")

    # check argument for number of parallel processes
    try:
        _max_workers = int(sys.argv[3])
        if _max_workers < 2 or _max_workers > 16:
            raise ValueError(f"Number of parallel processes is not valid. {ERROR_MSG}")
    except Exception:
        raise ValueError(f"Number of parallel processes is not valid. {ERROR_MSG}")

    main(_in_dir, _out_dir, _max_workers)
