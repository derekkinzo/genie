import pdb
import csv
import random
from connection import connection
from bigquery import client

results = client.query("""
    SELECT * FROM `harvard-599-trendsetters.aact.publications_cumulative_sum`
""")

with connection:
    with connection.cursor() as cur:
        cur.execute("DELETE FROM pub_sums;")
        connection.commit()
        count = 0

        for row in results:
            count += 1
            if count % 10000 == 0:
                print(count)
                connection.commit()
            cur.execute("INSERT INTO pub_sums VALUES (%s, %s, %s, %s);", (row[0], row[1], row[2] or 0, row[3] or 0))
