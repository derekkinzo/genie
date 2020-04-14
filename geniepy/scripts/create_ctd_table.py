import os
import pandas as pd
import gzip
from genieutils import decompress_gz

current_path = os.path.dirname(os.path.realpath(__file__))
CTD_DB_PATH = os.path.join(current_path, "CTD_genes_diseases.csv.gz")
CTD_PART = os.path.join(current_path, "CTD_genes_diseases_rows_12042020.csv")


row = 0
with gzip.open(CTD_DB_PATH, "r") as f_in:
    with open(CTD_PART, "w") as f_out:
        f_out.write(
            "TableRow,GeneSymbol,GeneID,DiseaseName,DiseaseID,DirectEvidence,InferenceChemicalName,InferenceScore,OmimIDs,PubMedIDs\n"
        )
        for line in f_in:
            line = line.decode("utf-8")
            if line.startswith("#"):  # Skip over comment lines
                continue
            row += 1
            record = f"{row}, " + line
            if row % 100000 == 0:
                print(f"{row} records processed")
            f_out.write(record)
