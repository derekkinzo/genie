import csv
import pdb
from connection import connection

with open("data/rankings", "r") as file:
    reader = csv.reader(file)
    with connection.cursor() as cur:
        cur.execute("DELETE FROM pubmed_ranks;")
        connection.commit()
        count = 0

        for row in reader:
            count += 1
            if count % 10000 == 0:
                print(count)
                connection.commit()
            cur.execute("INSERT INTO pubmed_ranks VALUES (%s, %s, %s);", (row[0], row[1], row[2]))
