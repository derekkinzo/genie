from flask import Flask, send_from_directory, request
from flask import render_template
from flask import jsonify
import datetime
import pdb
import statistics
from operator import itemgetter
import numpy as np
import csv
import random
import requests
from os import path
from bs4 import BeautifulSoup
import os

from genie import genie

# os.environ["FLASK_ENV"] = "development"

app = Flask("genie")
app.register_blueprint(genie)

app.run(host = "0.0.0.0", port = 5000)

@app.route("/search")
def search():
    q = request.args.get("q")
    results = []
    if path.exists("search_results/" + q):
        with open("search_results/" + q, "r") as results_file:
            reader = csv.reader(results_file)
            for row in reader:
                results.append(row)
    else:
        response = requests.get("https://www.googleapis.com/customsearch/v1?key=" + os.getenv("GOOGLE_API") + "&cx=004315576993373726096:gkqhc3opbnm&q=" + q)
        data = response.json()
        for item in data["items"]:
            results.append([item["title"], item["link"]])
        with open("search_results/" + q, "w") as results_file:
            writer = csv.writer(results_file)
            for result in results:
                writer.writerow(result)
    return jsonify(results)
