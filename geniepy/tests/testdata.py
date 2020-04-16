"""Module with data used in tests."""
import pandas as pd

CTD_INVALID_DF = [
    None,
    pd.DataFrame({"invalid": [1, 2]}),
    pd.DataFrame(
        {
            "GeneSymbol": ["11-BETA-HSD3"],
            "GeneID": ["A100174880"],  # Should be Int
            "DiseaseName": ["Abnormalities, Drug-Induced"],
            "DiseaseID": ["D000014"],
            "PubMedIDs": [22659286],
        }
    ),
    pd.DataFrame(
        {
            "GeneSymbol": ["11-BETA-HSD3"],
            "GeneID": [100174880.0],  # Should be Int
            "DiseaseName": ["Abnormalities, Drug-Induced"],
            "DiseaseID": ["D000014"],
            "PubMedIDs": [22659286],
        }
    ),
    pd.DataFrame(
        {
            "GeneSymbol": ["11-BETA-HSD3"],
            "GeneID": [100174880],
            "DiseaseName": ["Abnormalities, Drug-Induced"],
            "DiseaseID": ["MESH:D000014"],  # Should have "MESH:"
            "PubMedIDs": [22659286],
        }
    ),
    pd.DataFrame(
        {
            "GeneSymbol": ["11-BETA-HSD3"],
            "GeneID": [100174880],
            "DiseaseName": ["Abnormalities, Drug-Induced"],
            "DiseaseID": ["D000014"],
            "PubMedIDs": ["22659286"],  # Should be Int
        }
    ),
]

CTD_VALID_DF = [
    pd.DataFrame(
        {
            "GeneSymbol": ["11-BETA-HSD3"],
            "GeneID": [100174880],
            "DiseaseName": ["Abnormalities, Drug-Induced"],
            "DiseaseID": ["D000014"],
            "PubMedIDs": [22659286],
        }
    )
]
