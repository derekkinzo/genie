import datetime
import pdb
import numpy as np
import csv
import struct

with open("data/citations2.csv", "r") as rfile:
    reader = csv.reader(rfile)
    max = 0
    for row in reader:
        if int(row[0]) > max:
            max = int(row[0])
        for i in row[1]:
            if int(i) > max:
                max = int(i)

with open("data/citations2.csv", "r") as rfile:
    with open("data/links", "wb") as wfile:
        reader = csv.reader(rfile)
        wfile.write(max.to_bytes(4, signed=False, byteorder="little"))
        #
        # max = 0
        # for row in reader:
        #     if int(row[0]) > max:
        #         max = int(row[0])
        #     for i in row[1]:
        #         if int(i) > max:
        #             max = int(i)

#                 wfile.write()
#                 cited.add(row[0])
#                 for i in row[1:]:
#                     citer.add(i)
#                 count += 1
#                 if count % 100000 == 0:
#                     print(count)
#
#         wfile.write(struct.pack('i', value))
#
#
# for c in cited:
#     if not c in citer:
#         print(c)
