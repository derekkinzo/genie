import csv
import pdb

with open("data/genes.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    with open("data/gene_names.csv", "w") as file:
        writer = csv.writer(file)
        for row in reader:
            names = row[2].split("|")
            names.append(row[1])
            row = [row[0]]
            for name in names:
                name = name.strip().lower()
                if len(name) > 1:
                    row.append(name)
            writer.writerow(row)
