"""
Module to extract citation metadata for a given range of PubMed articles.

This script depends upon Google cloud function to scale-up the extraction process.
Make sure the Google cloud functions are deployed and available before running
this script. (See: citation_cloud_function.py)
"""
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime
from random import randint
import json
import os
import sys
import time
import requests

# Constants
_MIN_PUBMED_ID = 1
_MAX_PUBMED_ID = 40000000
_CHUNK_SIZE = 10
_CSV_SEPRATOR = "|"


# Google Cloud Functions - to scale-up data extraction
CLOUD_FN_1 = (
    "https://us-central1-csci-e-599-trend-detection.cloudfunctions.net/get_citation_1"
)
CLOUD_FN_2 = (
    "https://us-central1-csci-e-599-trend-detection.cloudfunctions.net/get_citation_2"
)
CLOUD_FN_3 = (
    "https://us-central1-csci-e-599-trend-detection.cloudfunctions.net/get_citation_3"
)
CLOUD_FN_4 = (
    "https://us-central1-csci-e-599-trend-detection.cloudfunctions.net/get_citation_4"
)
CLOUD_FN_5 = (
    "https://us-central1-csci-e-599-trend-detection.cloudfunctions.net/get_citation_5"
)
CLOUD_FN_6 = (
    "https://us-central1-csci-e-599-trend-detection.cloudfunctions.net/get_citation_6"
)
CLOUD_FN_7 = (
    "https://us-central1-csci-e-599-trend-detection.cloudfunctions.net/get_citation_7"
)
CLOUD_FN_8 = (
    "https://us-central1-csci-e-599-trend-detection.cloudfunctions.net/get_citation_8"
)
CLOUD_FN_9 = (
    "https://us-central1-csci-e-599-trend-detection.cloudfunctions.net/get_citation_9"
)
CLOUD_FN_10 = (
    "https://us-central1-csci-e-599-trend-detection.cloudfunctions.net/get_citation_10"
)

citation_dict = {}


def generate_ID_List(StartID, EndID):
    id_list = list(range(StartID, EndID + 1))
    chucked_id_list = [
        id_list[i * _CHUNK_SIZE : (i + 1) * _CHUNK_SIZE]  # noqa
        for i in range((len(id_list) + _CHUNK_SIZE - 1) // _CHUNK_SIZE)
    ]
    return chucked_id_list


def get_random_fn():
    # pick a random number between 1 and 5
    num = randint(1, 10)

    # return a randomly selected cloud function
    if num == 1:
        return CLOUD_FN_1
    elif num == 2:
        return CLOUD_FN_2
    elif num == 3:
        return CLOUD_FN_3
    elif num == 4:
        return CLOUD_FN_4
    elif num == 5:
        return CLOUD_FN_5
    elif num == 6:
        return CLOUD_FN_6
    elif num == 7:
        return CLOUD_FN_7
    elif num == 8:
        return CLOUD_FN_8
    elif num == 9:
        return CLOUD_FN_9
    else:
        return CLOUD_FN_10


def get_citation(IDList):
    ids_str = ",".join([str(elem) for elem in IDList])
    print(f"PID {os.getpid()}: Process Articles: {ids_str}")

    # construct api
    api_headers = {"content-type": "application/json"}
    api_body = {"pubmed_ids": ids_str}

    # call api - loop untill sucessful
    success = False
    while not success:
        cloud_fn = get_random_fn()
        try:
            req = requests.post(
                url=cloud_fn,
                data=json.dumps(api_body),
                headers=api_headers,
                timeout=(2, 5),
            )
            if req.status_code == 200:
                return req.text
        except Exception:
            """ if request fails or timeout, wait sometime and try again
            with another randomly selected cloud function """
            time.sleep(2)


def check_zero_citations(citationList):
    if not citationList or len(citationList) <= 0 or citationList == ["0"]:
        return True

    return False


def write_output(citation_dict, OutputDir):
    out_file = f"output-{datetime.now().microsecond}.csv"
    out_path = os.path.join(OutputDir, out_file)
    with open(out_path, "w") as file:
        file.write(
            "article_id"
            + _CSV_SEPRATOR
            + "cited_count"
            + _CSV_SEPRATOR
            + "cited_by_id"
            + "\n"
        )
        for key in citation_dict:
            if not check_zero_citations(citation_dict[key]):
                file.write(
                    key
                    + _CSV_SEPRATOR
                    + str(len(citation_dict[key]))
                    + _CSV_SEPRATOR
                    + ",".join(citation_dict[key])
                    + "\n"
                )
        print(
            f"Output: Citation data for {len(citation_dict)} \
PubMed Articles saved in file: {out_path}"
        )


def main(IDList, MaxWorkers, OutputDir):
    # start parallel processing
    with ProcessPoolExecutor(max_workers=MaxWorkers) as executor:
        result = executor.map(get_citation, IDList)

    # join parallel processing results
    for value in result:
        citation_dict.update(json.loads(value))

    # write json output
    write_output(citation_dict, OutputDir)


if __name__ == "__main__":  # noqa

    # command line arguments
    _start_id = 0
    _end_id = 0
    _max_workers = 0
    _out_dir = ""

    ERROR_MSG = """Command line arguments expected:
    <Start PubMed ID (ex: 1001)>,
    <End PubMed ID (ex: 1999)>,
    <Number of Parallel Processes (ex: 2-16)>
    <Output Directory (ex: ./data/)"""

    # check number if command line arguments
    if not sys.argv or len(sys.argv) < 5:
        raise ValueError(ERROR_MSG)

    # check command line argument for Start PubMed ID
    try:
        _start_id = int(sys.argv[1])
    except Exception:
        raise ValueError(f"Start PubMed ID is not valid. {ERROR_MSG}")

    # check command line argument for Start PubMed ID between allowed min and max values
    if _start_id < _MIN_PUBMED_ID or _start_id > (_MAX_PUBMED_ID - 1):
        raise ValueError(
            f"Start PubMed ID should be between {_MIN_PUBMED_ID} \
and {_MAX_PUBMED_ID-1}.  {ERROR_MSG}"
        )

    # check command line argument for End PubMed ID
    try:
        _end_id = int(sys.argv[2])
    except Exception:
        raise ValueError(f"End PubMed ID is not valid. {ERROR_MSG}")

    # check command line argument for End PubMed ID between allowed min and max values
    if _end_id < (_MIN_PUBMED_ID + 1) or _end_id > _MAX_PUBMED_ID:
        raise ValueError(
            f"End PubMed ID should be between {_MIN_PUBMED_ID+1} and {_MAX_PUBMED_ID}"
        )

    # check command line argument for Start PubMed ID < End PubMed ID
    if _start_id > _end_id:
        raise ValueError(
            f"End PubMed ID should be greater than Start PubMed ID. {ERROR_MSG}"
        )

    # check command line argument for Parallel Workers
    try:
        _max_workers = int(sys.argv[3])
    except Exception:
        raise ValueError(f"Number of parallel workers is not valid. {ERROR_MSG}")

    # check command line argument for Parallel Workers is between 2 and 16
    if _max_workers < 2 or _max_workers > 16:
        raise ValueError(
            f"Number of parallel workers should be between 2 and 16. {ERROR_MSG}"
        )

    # check command line argument for Output Directory is valid
    _out_dir = sys.argv[4]
    if not os.path.isdir(_out_dir):
        raise ValueError(f"Output data directory is not valid. {ERROR_MSG}")

    start_time = datetime.now()
    main(generate_ID_List(_start_id, _end_id), _max_workers, _out_dir)

    tot_time = datetime.now() - start_time
    print(
        f"Processed {_end_id-_start_id+1} PubMed Articles in \
{round(tot_time.total_seconds()/60,2)} minutes"
    )
