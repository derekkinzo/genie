import csv
import pdb
from nltk.corpus import words

words = set(words.words())
words.add("pdb")

with open("data/genes.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    with open("data/gene_names.csv", "w") as file:
        writer = csv.writer(file)
        for row in reader:
            names = [row[1]]
            for synonym in row[2].split("|"):
                synonym = synonym.strip()
                if len(synonym) > 4:
                    names.append(synonym)
            row = [row[0]]
            for name in names:
                name = name.lower()
                if name not in words:
                    row.append(name)
            writer.writerow(row)
