import pdb
import csv
import random
from connection import connection
from bigquery import client

results = client.query("""
    SELECT * FROM `harvard-599-trendsetters.aact.cumulative_sjr_stats`
""")

with connection:
    with connection.cursor() as cur:
        cur.execute("DELETE FROM sjr_stats;")
        connection.commit()
        count = 0

        for row in results:
            count += 1
            if count % 10000 == 0:
                print(count)
                connection.commit()

            if row[1].isdigit():
                cur.execute("INSERT INTO sjr_stats VALUES (%s, %s, %s, %s, %s, %s);", (row[0], row[1], row[2], row[3], row[4], row[5]))
