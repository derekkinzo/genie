import datetime
import pdb
import numpy as np
import csv
import struct

articles = set()
max = 0

with open("data/citations.csv", "r") as rfile:
    reader = csv.reader(rfile)
    count = 0
    for row in reader:
        count += 1
        if count % 100000 == 0:
            print(count)
        cited = int(row[0])
        articles.add(cited)
        if cited > max:
            max = cited
        for i in row[1:]:
            citer = int(i)
            articles.add(citer)
            if citer > max:
                max = citer

with open("data/citations.csv", "r") as rfile:
    reader = csv.reader(rfile)
    with open("data/links", "wb") as wfile:
        wfile.write(max.to_bytes(4, signed=False, byteorder="little"))
        wfile.write(len(articles).to_bytes(4, signed=False, byteorder="little"))
        print(len(articles))
        print(max)
        count = 0
        for row in reader:
            wfile.write(int(row[0]).to_bytes(4, signed=False, byteorder="little"))
            wfile.write(len(row[1:]).to_bytes(4, signed=False, byteorder="little"))
            count += 1
            if count % 100000 == 0:
                print(count)
            for i in row[1:]:
                wfile.write(int(i).to_bytes(4, signed=False, byteorder="little"))
