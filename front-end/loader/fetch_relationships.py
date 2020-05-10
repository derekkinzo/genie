import pdb
import csv
import random
from connection import connection
from bigquery import client

results = client.query("""
    SELECT * FROM `harvard-599-trendsetters.Genie.final_table_output_to_ui`
""")

with connection:
    with connection.cursor() as cur:
        cur.execute("DELETE FROM relationships;")
        connection.commit()

        count = 0
        for row in results:
            count += 1
            if count % 5000 == 0:
                print(count)
                connection.commit()

            change_recent = None
            if row[6] == "N":
                change_recent = False
            elif row[6] == "Y":
                change_recent = True
            cur.execute(
                "INSERT INTO relationships VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT (id) DO NOTHING;",
                (row[0], row[1][:-1], row[2], row[3], row[4] or "", row[5] or "", change_recent, row[7] and row[7][:-1] or 0, row[8] and row[8][:-1] or 0, row[9], row[10] or 0)
            )
