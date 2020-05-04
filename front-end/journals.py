from flask import Flask, send_from_directory, request
from flask import render_template
from flask import jsonify
from flask import Blueprint
import pdb
from connection import connection
journals = Blueprint("journals", __name__)
orders = [None, "ASC", "DESC"]
columns = ["Gene Disease", "Year", "Count"]
cols = [None, "year", "count"]

@journals.route("/journals/view")
def view():
    return render_template("journals.html", columns = columns)

@journals.route("/journals")
def index():
    search = request.args.get("search")
    order = "id, year"
    if request.args.get("sortcol"):
        order = f"{cols[int(request.args.get('sortcol'))]} {orders[int(request.args.get('sortstate'))]}, " + order

    with connection as conn:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, year, count
                FROM journals
                WHERE id LIKE %(search)s
                ORDER BY {}
                LIMIT 100
                OFFSET 0;
            """.format(order), {"search": f"%{search}%"})
            journals = cur.fetchall()
            results = []
            for journal in journals:
                results.append(journal)
            return jsonify(results)
