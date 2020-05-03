import pdb
import csv
import random
from connection import connection
from bigquery import client

results = client.query("""
    SELECT * FROM `harvard-599-trendsetters.aact.cumulative_journals`
""")

with connection:
    with connection.cursor() as cur:
        cur.execute("DELETE FROM journals;")
        connection.commit()
        count = 0

        for row in results:
            count += 1
            if count % 5000 == 0:
                print(count)
                connection.commit()
            cur.execute("INSERT INTO journals VALUES (%s, %s, %s);", (row[0], row[1], row[2]))
