from flask import Flask, send_from_directory, request, make_response
from flask import render_template
from flask import jsonify
from flask import Blueprint
import pdb
import math
import numpy as np
from connection import connection
from os import path
import csv
import io

genie = Blueprint("genie", __name__)
orders = [None, "DESC", "ASC"]
num_columns = 10
column_names = ["Id", "P2 Prob", "Mesh Id", "Disease", "Gene", "Change Recent", "Probability Change", "Previous Probability", "Publications", "Citations"]
assert(len(column_names) == num_columns)
columns = ["id", "p2_prob", "mesh_id", "disease_name", "gene_name", "change_recent", "recent_prob_change", "previous_prob", "num_pubs", "num_citations"]
assert(len(columns) == num_columns)
sorts = [False, True, False, False, False, True, True, True, True, True]
assert(len(sorts) == num_columns)
searches = [True, False, True, True, True, False, False, False, False, False]
assert(len(searches) == num_columns)

@genie.route("/")
def view():
    return render_template("index.html", column_names = column_names, sorts = sorts)

@genie.route("/relationships")
def index():
    where_sql = None
    if request.args.get("search") and len(request.args.get("search")) >= 3:
        where_sql = "WHERE "
        for i in range(num_columns):
            if searches[i]:
                where_sql += "{} ILIKE %(query)s OR ".format(columns[i])
        where_sql = where_sql[:-3]

    order = "p2_prob DESC, id"
    page = int(request.args.get("page"))

    if request.args.get("sortcolumn"):
        order = "{} {}, ".format(columns[int(request.args.get('sortcolumn'))], orders[int(request.args.get('sortstate'))]) + order

    with connection as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT {}
                FROM relationships
                {}
                ORDER BY {}
                LIMIT {}
                OFFSET {};
            """.format(", ".join(columns), where_sql, order, 50, page * 50), {"query": "%{}%".format(request.args.get("search"))})
            relationships = cur.fetchall()
            results = []
            for relationship in relationships:
                row = list(relationship)
                row[1] = str(row[1]) + "%"
                row[6] = str(row[6]) + "%"
                row[7] = str(row[7]) + "%"
                results.append(row)

            if request.args.get("format") == "csv":
                file_data = io.StringIO()
                writer = csv.writer(file_data)
                writer.writerow(column_names)
                for row in results:
                    writer.writerow(row)
                response = make_response(file_data.getvalue())
                response.headers["Content-Disposition"] = "attachment; filename=data.csv"
                response.headers["Content-type"] = "text/csv"
                return response

            cur.execute("""
                SELECT count(1)
                FROM relationships
                {};
            """.format(where_sql), {"query": "%{}%".format(request.args.get("search"))})
            count = cur.fetchone()[0]

            return jsonify({"items": results, "total_pages": math.ceil(count / 50)})

@genie.route("/relationships/<path:id>")
def show(id):
    with connection as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT gene_id, mesh_id, gene_name, disease_name FROM relationships WHERE id = %s;", (id, ))
            relationship = cur.fetchone()

            cur.execute("SELECT year, pmid_cum_sum, citations_cum_sum FROM gene_pubs WHERE id = %s;", (relationship[0], ))
            gene_data = np.array(cur.fetchall()).T

            cur.execute("SELECT year, pmid_cum_sum, citations_cum_sum FROM disease_pubs WHERE id = %s;", (relationship[1], ))
            disease_data = np.array(cur.fetchall()).T

            cur.execute("SELECT year, hindex, sjr FROM sjr_stats WHERE id = %s ORDER BY year;", (id, ))
            sjr_data = np.array(cur.fetchall()).T.tolist()

            cur.execute("SELECT year, pmid_sum, citations_sum FROM pub_sums WHERE id = %s ORDER BY year;;", (id, ))
            pubs_data = np.array(cur.fetchall()).T.tolist()

            cur.execute("SELECT year, journal_sum FROM journal_sums WHERE id = %s ORDER BY year;", (id, ))
            journals_data = np.array(cur.fetchall()).T.tolist()

            stats = {
                "HIndex": (sjr_data[0], sjr_data[1]),
                "SJR": (sjr_data[0], sjr_data[2]),
                "Total Publications": (pubs_data[0], pubs_data[1]),
                "Total Citations": (pubs_data[0], pubs_data[2]),
                "Total Journal": (journals_data[0], journals_data[1])
            }

            return jsonify({"gene_data": gene_data.tolist(), "disease_data": disease_data.tolist(), "gene_name": relationship[2], "disease_name": relationship[3], "stats": stats})


@genie.route("/search")
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
