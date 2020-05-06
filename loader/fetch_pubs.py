import pdb
import csv
import random
from connection import connection
from bigquery import client

with connection:
    with connection.cursor() as cur:
        for type in ["gene", "disease"]:
            results = client.query("""
                SELECT * FROM `harvard-599-trendsetters.aact.cumulative_{}_publications` LIMIT 1000
            """.format(type))

            cur.execute("DELETE FROM {}_pubs;".format(type))
            connection.commit()

            count = 0
            for row in results:
                count += 1
                if count % 5000 == 0:
                    print(count)
                    connection.commit()
                cur.execute(
                    "INSERT INTO {}_pubs VALUES (%s, %s, %s, %s);".format(type),
                    (row[0], row[1], row[2] or 0, row[3] or 0)
                )
