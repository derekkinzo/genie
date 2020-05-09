import datetime
import pdb
import numpy as np
import csv
import random
import requests
from os import path
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.dirname(os.getcwd()) + "/service-account.json"
from google.cloud import bigquery
client = bigquery.Client()

results = client.query("""
    SELECT `pmid`, `citation_pmid` FROM `harvard-599-trendsetters.pubmed.pubmed_citation`
""")

with open("data/citations.csv", "w") as file:
    writer = csv.writer(file)
    count = 0
    for row in results:
        data = [int(row[0])]
        for i in row[1].split(","):
            data.append(int(i))
        count += 1
        if count % 10000 == 0:
            print(count)
        writer.writerow(data)
