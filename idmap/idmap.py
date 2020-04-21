import datetime
import pdb
import numpy as np
import csv
import random
import requests
from os import path
import os
from dictionary import dictionary

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getcwd() + "/service-account.json"
from google.cloud import bigquery

client = bigquery.Client()
offset = 0
limit = 5000

def map():
    results = client.query("""
        SELECT pmid, abstract FROM `harvard-599-trendsetters.pubmed.baseline_02032020` LIMIT 1000
    """).result()
    for row in results:
        abstract = row[1].lower()
        for i in range(len(abstract)):
            current = dictionary
            for k in range(i, len(abstract)):
                if abstract[k] not in current:
                    break
                current = current[abstract[k]]
                if chr(0) in current:
                    print(row[0], abstract[i:k + 1])

map()
