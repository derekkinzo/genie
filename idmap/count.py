import datetime
import pdb
import numpy as np
import csv
import random
import requests
from os import path
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getcwd() + "/service-account.json"
from google.cloud import bigquery

client = bigquery.Client()

def write_count():
    count = query_job = client.query("""
        SELECT count(*) FROM `harvard-599-trendsetters.pubmed.baseline_02032020`
    """).result()
    for row in count:
        with open("data/count", "w") as file:
            return file.write(str(row[0]))

if not os.path.isfile("data/count"):
    write_count()

count = 0
with open("data/count", "r") as file:
    count = int(file.read())
