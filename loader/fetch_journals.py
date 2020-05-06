import pdb
import csv
import random
from connection import connection
from bigquery import client

results = client.query("""
    SELECT * FROM `harvard-599-trendsetters.aact.cumulative_journals` LIMIT 1000
""")

with connection:
    with connection.cursor() as cur:
        cur.execute("DELETE FROM journal_sums;")
        connection.commit()
        count = 0

        for row in results:
            count += 1
            if count % 10000 == 0:
                print(count)
                connection.commit()
            cur.execute("INSERT INTO journal_sums VALUES (%s, %s, %s);", (row[0], row[1], row[2]))
