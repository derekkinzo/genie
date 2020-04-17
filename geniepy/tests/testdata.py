"""Module with data used in tests."""
import pandas as pd

CTD_INVALID_DAO = [
    pd.DataFrame(
        {
            # Missing Digest required field
            "GeneSymbol": ["11-BETA-HSD3"],
            "GeneID": [100174880],
            "DiseaseName": ["Abnormalities, Drug-Induced"],
            "DiseaseID": ["D000014"],
            "PubMedIDs": ["22659286"],
        }
    ),
    pd.DataFrame(
        {
            "OtherField": [22659286],  # Non-existent schema column
            "Digest": [22659286],
            "GeneSymbol": ["11-BETA-HSD3"],
            "GeneID": [100174880],
            "DiseaseName": ["Abnormalities, Drug-Induced"],
            "DiseaseID": ["D000014"],
            "PubMedIDs": ["22659286"],
        }
    ),
    pd.DataFrame(
        {
            "Digest": [22659286],
            "GeneSymbol": ["11-BETA-HSD3"],
            # Missing required GeneID
            "DiseaseName": ["Abnormalities, Drug-Induced"],
            "DiseaseID": ["D000014"],
            "PubMedIDs": ["22659286"],
        }
    ),
    pd.DataFrame(
        {
            "Digest": [22659286],
            "GeneSymbol": ["11-BETA-HSD3"],
            "GeneID": [100174880],
            "DiseaseName": ["Abnormalities, Drug-Induced"],
            # Missing required DiseaseID
            "PubMedIDs": ["22659286"],
        }
    ),
    pd.DataFrame(
        {
            "Digest": [22659286],
            "GeneSymbol": ["11-BETA-HSD3"],
            "GeneID": [100174880],
            "DiseaseName": ["Abnormalities, Drug-Induced"],
            "DiseaseID": ["D000014"],
            # Missing required PubMed
        }
    ),
]
"""Invalid DAO record."""

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
            "PubMedIDs": ["22659286"],
        }
    ),
    pd.DataFrame(
        {
            "Digest": [22659286],
            "GeneSymbol": ["11-BETA-HSD3"],
            "GeneID": [100174880.0],  # Should be Int
            "DiseaseName": ["Abnormalities, Drug-Induced"],
            "DiseaseID": ["D000014"],
            "PubMedIDs": ["22659286"],
        }
    ),
    pd.DataFrame(
        {
            "Digest": [22659286],
            "GeneSymbol": ["11-BETA-HSD3"],
            "GeneID": [100174880],
            "DiseaseName": ["Abnormalities, Drug-Induced"],
            "DiseaseID": ["MESH:D000014"],  # Should not have "MESH:"
            "PubMedIDs": ["22659286"],
        }
    ),
] + CTD_INVALID_DAO
"""Array of invalid DataFrames because violate parser rules."""


CTD_VALID_DF = [
    pd.DataFrame(
        {
            "Digest": [
                "b3834d9281286247e377c5700e9689c3660412df24fa0a4921c6e3c213d616aa"
            ],
            "GeneSymbol": ["11-BETA-HSD3"],
            "GeneID": [10174880],
            "DiseaseName": ["Abnormalities, Drug-Induced"],
            "DiseaseID": ["D000014"],
            "PubMedIDs": ["22659286"],
        }
    ),
    pd.DataFrame(
        {
            "Digest": [
                "e96cc1eb2423dad1fd6f4f341574fbb7fff0479a3339c9e2e4f814f2d970e3f00"
            ],
            "GeneSymbol": ["1-SF3"],
            "GeneID": [1000494280],
            "DiseaseName": ["Infant Death"],
            "DiseaseID": ["D0660884"],
            "PubMedIDs": ["283930756"],  # PubMedId can be int or str
        }
    ),
    pd.DataFrame(
        {
            "Digest": [
                "e120bfecd61ee146bb3a4c61f8dbb93754b1db25f62aba505872ef5568dd155b"
            ],
            "GeneSymbol": ["11-BETA-HSD3"],
            "GeneID": [100174880],
            "DiseaseName": ["Abnormalities, Drug-Induced"],
            "DiseaseID": ["D000014"],
            "PubMedIDs": ["22659286"],  # PubMedId can be int or str
        }
    ),
    pd.DataFrame(
        {
            "Digest": [
                "f847dcfeaaae8fefa96e1f6e97dd5998ffe07365d1254badae927d1769a2eebc"
            ],
            "GeneSymbol": ["A1BG3"],
            "GeneID": [1],
            "DiseaseName": ["Muscle Weaknessd"],
            "DiseaseID": ["D0189084"],
            "PubMedIDs": ["3515563|54800|62135|63766|6511338|7995496"],
        }
    ),
]
"""Array of valid DataFrames."""
