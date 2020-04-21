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
        SELECT pmid, abstract FROM `harvard-599-trendsetters.pubmed.baseline_02032020`
    """).result()
    with open("data/abstract_genes.csv", "w") as file:
        writer = csv.writer(file)
        for row in results:
            if not row[1]:
                continue
            abstract = row[1].lower() + " "
            results = [row[0]]
            for i in range(len(abstract) - 1):
                if not abstract[i - 1].isalpha():
                    current = dictionary
                    for k in range(i, len(abstract)):
                        if abstract[k] not in current:
                            break
                        current = current[abstract[k]]
                        if chr(0) in current and not abstract[k + 1].isalpha():
                            results.append(row[1][i:k + 1])
            writer.writerow(results)

map()
