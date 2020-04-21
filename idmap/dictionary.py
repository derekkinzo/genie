import csv
import pdb

import csv
import pdb

dictionary = dict()
min_ord = 256
max_ord = 0

with open("data/gene_names.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        names = row[1:]
        for name in names:
            current = dictionary
            for char in name:
                if char not in current:
                    current[char] = {}
                current = current[char]
            current[chr(0)] = chr(0)
