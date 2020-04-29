"""
This script is deployed as Google Cloud Function.

It allows to scale-up the citation metadata extraction process.
This script also utilizes multiple PubMed API Keys, to scale-up the number of API
calls that can be made per second. Plesae make sure the API Keys included are
valid before executing this script.
"""
from flask import abort
import json
from random import randint
import requests
import xml.etree.ElementTree as ET

# Constants
API_BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?dbfrom=pubmed&linkname=pubmed_pubmed_citedin"  # noqa
API_ID_PARAM = "&id="
API_KEY_PARAM = "&api_key="
API_KEY_1 = "70b53d4e84436970587aef3493a723cae708"
API_KEY_2 = "9ab4b04dcabcab740d1a297e6f3f54aa1e09"
API_KEY_3 = "39458b83e654b32523475ee6b828b6c22c08"
API_KEY_4 = "cf95d471b41c4ea9e6b89d41de269705eb08"
API_KEY_5 = "94c3049a7b3dffca2d22ce11b51a3ea5da09"
API_KEY_6 = "3fb37654e8f711f8751d9e3c21fc46257108"
API_KEY_7 = "91315e4e69c1b5e2676371490cfc715caa08"
API_KEY_8 = "b1ee76fae01c312e4bf2fd3e8b1bcf978a09"
API_KEY_9 = "25b74bb456d7e6fc756c86c7aebb1b525009"
API_KEY_10 = "7a7e4492084dd09cef758ee65a7909704b08"
API_KEY_11 = "4d32405f13fed69766ad639d89c5c5288608"
API_KEY_12 = "18c8d26e60b5cd012e2ba9618c88dd12cb09"
API_KEY_13 = "667ca5b1b72b7697ed43c26727329282bb08"
API_KEY_14 = "5cdea4b682e2fc93c56c2b1e5e9da93f4709"
API_KEY_15 = "108b2e1a81369991da6c737545097c581a08"
API_KEY_16 = "f10805158a7609bb115cb074b05e5923a407"
API_KEY_17 = "00d74dd1cb732cd7fc29f54168fe7055c809"
TAG_LINK_SET = "LinkSet"
TAG_ID = "./IdList/Id"
TAG_CITATION_ID = "./LinkSetDb/Link/Id"


def get_random_api_key():  # noqa
    # pick a random number between 1 and 5
    num = randint(1, 17)
    # return a randomly selected cloud function
    if num == 1:
        return API_KEY_1
    elif num == 2:
        return API_KEY_2
    elif num == 3:
        return API_KEY_3
    elif num == 4:
        return API_KEY_4
    elif num == 5:
        return API_KEY_5
    elif num == 6:
        return API_KEY_6
    elif num == 7:
        return API_KEY_7
    elif num == 8:
        return API_KEY_8
    elif num == 9:
        return API_KEY_9
    elif num == 10:
        return API_KEY_10
    elif num == 11:
        return API_KEY_11
    elif num == 12:
        return API_KEY_12
    elif num == 13:
        return API_KEY_13
    elif num == 14:
        return API_KEY_14
    elif num == 15:
        return API_KEY_15
    elif num == 16:
        return API_KEY_16
    else:
        return API_KEY_17


def parse_citation(url: str):

    _citation_dict = {}

    try:
        req = requests.get(url)
        tree = ET.fromstring(req.text)
    except Exception:
        print(f"Exeception: bad request: {url}")
        return _citation_dict

    for linkSet in tree.findall(TAG_LINK_SET):
        _pubmed_id = linkSet.find(TAG_ID).text
        _citation_id_list: str = []
        for citationId in linkSet.findall(TAG_CITATION_ID):
            _citation_id_list.append(citationId.text)

        if not _citation_id_list or len(_citation_id_list) <= 0:
            _citation_id_list.append("0")

        _citation_dict[_pubmed_id] = _citation_id_list

    return _citation_dict


def get_citation(request):
    if request.method != "POST":
        return abort(405)

    # get list of PubMed IDs from the request body
    request_json = request.get_json()
    pubmed_ids = request_json["pubmed_ids"]

    # split PubMed IDs and construct ID Parameter list
    API_ID_PARAM_LIST = ""
    for pubmed_id in pubmed_ids.split(","):
        API_ID_PARAM_LIST = API_ID_PARAM_LIST + API_ID_PARAM + pubmed_id

    # get random API Key
    API_KEY = get_random_api_key()

    # construct API url
    url = API_BASE_URL + API_KEY_PARAM + API_KEY + API_ID_PARAM_LIST

    return json.dumps(parse_citation(url))
