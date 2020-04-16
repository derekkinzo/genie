"""Module with data used in tests."""
import pandas as pd

CTD_INVALID_DF = [
    None,
    pd.DataFrame({"invalid": [1, 2]}),
    pd.DataFrame(
        {
            "Digest": [22659286],
            "GeneSymbol": ["11-BETA-HSD3"],
            "GeneID": ["A100174880"],  # Should be Int
            "DiseaseName": ["Abnormalities, Drug-Induced"],
            "DiseaseID": ["D000014"],
            "PubMedIDs": [22659286],
        }
    ),
    pd.DataFrame(
        {
            "Digest": [22659286],
            "GeneSymbol": ["11-BETA-HSD3"],
            "GeneID": [100174880.0],  # Should be Int
            "DiseaseName": ["Abnormalities, Drug-Induced"],
            "DiseaseID": ["D000014"],
            "PubMedIDs": [22659286],
        }
    ),
    pd.DataFrame(
        {
            "Digest": [22659286],
            "GeneSymbol": ["11-BETA-HSD3"],
            "GeneID": [100174880],
            "DiseaseName": ["Abnormalities, Drug-Induced"],
            "DiseaseID": ["MESH:D000014"],  # Should not have "MESH:"
            "PubMedIDs": [22659286],
        }
    ),
    pd.DataFrame(
        {
            "Digest": ["22659286"],  # Should be int
            "GeneSymbol": ["11-BETA-HSD3"],
            "GeneID": [100174880],
            "DiseaseName": ["Abnormalities, Drug-Induced"],
            "DiseaseID": ["D000014"],
            "PubMedIDs": [22659286],
        }
    ),
]

CTD_VALID_DF = [
    pd.DataFrame(
        {
            "Digest": [22659286],
            "GeneSymbol": ["11-BETA-HSD3"],
            "GeneID": [100174880],
            "DiseaseName": ["Abnormalities, Drug-Induced"],
            "DiseaseID": ["D000014"],
            "PubMedIDs": [22659286],
        }
    ),
    pd.DataFrame(
        {
            "Digest": [22659286],
            "GeneSymbol": ["1-SF3"],
            "GeneID": [1000494280],
            "DiseaseName": ["Infant Death"],
            "DiseaseID": ["D0660884"],
            "PubMedIDs": [283930756],  # PubMedId can be int or str
        }
    ),
    pd.DataFrame(
        {
            "Digest": [22659286],
            "GeneSymbol": ["11-BETA-HSD3"],
            "GeneID": [100174880],
            "DiseaseName": ["Abnormalities, Drug-Induced"],
            "DiseaseID": ["D000014"],
            "PubMedIDs": ["22659286"],  # PubMedId can be int or str
        }
    ),
    pd.DataFrame(
        {
            "Digest": [22659286],
            "GeneSymbol": ["A1BG3"],
            "GeneID": [1],
            "DiseaseName": ["Muscle Weaknessd"],
            "DiseaseID": ["D0189084"],
            "PubMedIDs": ["3515563|54800|62135|63766|6511338|7995496"],
        }
    ),
]
