from os import path
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.dirname(os.getcwd()) + "/service-account.json"
from google.cloud import bigquery
client = bigquery.Client()
