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
import os
from waitress import serve

from genie import genie

# os.environ["FLASK_ENV"] = "development"

app = Flask("genie")
app.register_blueprint(genie)

if "PRODUCTION" in os.environ:
    serve(app, host='0.0.0.0', port="PORT" in os.environ and os.environ["PORT"] or 5000)
else:
    app.run(host = "0.0.0.0", port = "PORT" in os.environ and os.environ["PORT"] or 5000)
