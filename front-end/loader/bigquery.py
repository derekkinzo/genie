from os import path
import os
import pdb
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getcwd() + "/service-account.json"
from google.cloud import bigquery
client = bigquery.Client()
