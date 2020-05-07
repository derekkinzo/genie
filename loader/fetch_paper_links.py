import pdb
import csv
import random
from connection import connection
from bigquery import client

results = client.query("""
    SELECT * FROM `harvard-599-trendsetters.Genie.ui_papers_links`
""")

with connection:
    with connection.cursor() as cur:
        cur.execute("DELETE FROM paper_links;")
        connection.commit()
        count = 0

        for row in results:
            count += 1
            if count % 10000 == 0:
                print(count)
                connection.commit()
            if row[6]:
                cur.execute("INSERT INTO paper_links VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT (id) DO NOTHING;", (row[0], row[1], row[2], row[3], row[4], row[5] or 0, row[6], row[7]))
