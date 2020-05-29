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
import requests
import os

genie = Blueprint("genie", __name__)
orders = [None, "DESC", "ASC"]
column_names = ["Id", "Mesh Id", "Disease", "Gene", "P2 Prob", "Change Recent", "Probability Change", "Previous Probability", "Publications", "Citations"]
columns = ["id", "mesh_id", "disease_name", "gene_name", "p2_prob", "change_recent", "recent_prob_change", "previous_prob", "num_pubs", "num_citations"]
column_types = ["text", "text", "text", "text", "numeric", "boolean", "numeric", "numeric", "numeric", "numeric"]

@genie.route("/")
def view():
    return render_template("index.html", column_names = column_names, column_types = column_types)

@genie.route("/relationships")
def index():
    where_statements = []
    where_values = dict()
    for i in range(1, len(column_types)):
        search = request.args.get("search[{}]".format(i))
        if column_types[i] == "text":
            if len(search) >= 3:
                where_statements.append("{} ILIKE %(where{})s".format(columns[i], i))
                where_values["where{}".format(i)] = "%{}%".format(search)
        elif column_types[i] == "numeric":
            min, max = search.split(":")
            min = min and float(min)
            max = max and float(max)
            if min:
                where_statements.append("{} >= {}".format(columns[i], min))
            if max:
                where_statements.append("{} <= {}".format(columns[i], max))

    where_sql = "WHERE " + " AND ".join(where_statements) if where_statements else ""
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
            """.format(", ".join(columns), where_sql, order, 50, page * 50), where_values)

            relationships = cur.fetchall()
            results = []
            for relationship in relationships:
                row = list(relationship)
                row[4] = str(row[4]) + "%"
                row[6] = str(row[6]) + "%"
                row[7] = str(row[7]) + "%"
                row[8] = "{:,}".format(row[8])
                row[9] = "{:,}".format(row[9])
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
            """.format(where_sql), where_values)

            cur.execute("""
                SELECT count(1)
                FROM relationships
                {};
            """.format(where_sql), where_values)
            count = cur.fetchone()[0]

            return jsonify({"items": results, "total_pages": math.ceil(count / 50)})

@genie.route("/relationships/<path:id>")
def show(id):
    with connection as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT gene_id, mesh_id, gene_name, disease_name FROM relationships WHERE id = %s;", (id, ))
            relationship = cur.fetchone()

            cur.execute("SELECT year, pmid_cum_sum, citations_cum_sum FROM gene_pubs WHERE id = %s;", (relationship[0], ))
            gene_data = np.array(cur.fetchall()).T.reshape(3, -1)

            cur.execute("SELECT year, pmid_cum_sum, citations_cum_sum FROM disease_pubs WHERE id = %s;", (relationship[1], ))
            disease_data = np.array(cur.fetchall()).T.reshape(3, -1)

            cur.execute("SELECT year, hindex, sjr FROM sjr_stats WHERE id = %s ORDER BY year;", (id, ))
            sjr_data = np.array(cur.fetchall()).T.reshape(3, -1).tolist()

            cur.execute("SELECT year, pmid_sum, citations_sum FROM pub_sums WHERE id = %s ORDER BY year;;", (id, ))
            pubs_data = np.array(cur.fetchall()).T.reshape(3, -1).tolist()

            cur.execute("SELECT year, journal_sum FROM journal_sums WHERE id = %s ORDER BY year;", (id, ))
            journals_data = np.array(cur.fetchall()).T.reshape(2, -1).tolist()

            cur.execute("""
                SELECT DISTINCT paper_links.title, paper_links.link, paper_links.citations, pubmed_ranks.pubmed_rank
                FROM paper_links LEFT OUTER JOIN pubmed_ranks
                ON paper_links.pmid = pubmed_ranks.id
                WHERE gene_id = %s
                ORDER BY pubmed_ranks.pubmed_rank DESC
                LIMIT 50;
            """, (relationship[0], ))
            gene_links = [[row[0], row[1], row[2], str(row[3])] for row in cur.fetchall()]


            cur.execute("""
                SELECT DISTINCT paper_links.title, paper_links.link, paper_links.citations, pubmed_ranks.pubmed_rank
                FROM paper_links LEFT OUTER JOIN pubmed_ranks
                ON paper_links.pmid = pubmed_ranks.id
                WHERE mesh_id = %s
                ORDER BY pubmed_ranks.pubmed_rank DESC
                LIMIT 50;
            """, (relationship[1], ))
            disease_links = [[row[0], row[1], row[2], str(row[3])] for row in cur.fetchall()]

            stats = [
                ("Total Publications", pubs_data[0], pubs_data[1], "Cumulative Count"),
                ("Total Citations", pubs_data[0], pubs_data[2], "Cumulative Count"),
                ("Total Journal", journals_data[0], journals_data[1], "Cumulative Count"),
                ("SJR", sjr_data[0], sjr_data[2], "Average"),
                ("h index", sjr_data[0], sjr_data[1], "Average")
            ]

            return jsonify({"gene_data": gene_data.tolist(), "disease_data": disease_data.tolist(), "gene_name": relationship[2], "disease_name": relationship[3], "stats": stats, "gene_links": gene_links, "disease_links": disease_links})


@genie.route("/search")
def search():
    q = request.args.get("q")

    if not path.exists("search_results/" + q):
        results = []
        response = requests.get("https://www.googleapis.com/customsearch/v1?key=" + os.getenv("GOOGLE_API") + "&cx=004315576993373726096:gkqhc3opbnm&q=" + q)
        data = response.json()
        for item in data["items"]:
            title = "".join(item["title"].split(" - ")[1:])
            results.append([title, item["link"]])
        with open("search_results/" + q, "w") as results_file:
            writer = csv.writer(results_file)
            for result in results:
                writer.writerow(result)

    results = []
    with open("search_results/" + q, "r") as results_file:
        reader = csv.reader(results_file)
        for row in reader:
            results.append(row)

    return jsonify(results)
