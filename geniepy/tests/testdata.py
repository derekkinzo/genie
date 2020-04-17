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
            "PubMedIDs": [22659286],
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
            "PubMedIDs": [22659286],
        }
    ),
    pd.DataFrame(
        {
            "Digest": [22659286],
            "GeneSymbol": ["11-BETA-HSD3"],
            # Missing required GeneID
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
            # Missing required DiseaseID
            "PubMedIDs": [22659286],
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
] + CTD_INVALID_DAO
"""Array of invalid DataFrames because violate parser rules."""


CTD_VALID_DF = [
    pd.DataFrame(
        {
            "Digest": [
                b"\xb3\x83M\x92\x81(bG\xe3w\xc5p\x0e\x96\x89\xc3f\x04\x12\xdf$\xfa\nI!\xc6\xe3\xc2\x13\xd6\x16\xaa"
            ],
            "GeneSymbol": ["11-BETA-HSD3"],
            "GeneID": [10174880],
            "DiseaseName": ["Abnormalities, Drug-Induced"],
            "DiseaseID": ["D000014"],
            "PubMedIDs": [22659286],
        }
    ),
    pd.DataFrame(
        {
            "Digest": [
                b"\xe9l\xc1\xeb$#\xda\xd1\xfdoO4\x15t\xfb\xb7\xff\xf0G\x9a39\xc9\xe2\xe4\xf8\x14\xf2\xd9p\xe3\xf0"
            ],
            "GeneSymbol": ["1-SF3"],
            "GeneID": [1000494280],
            "DiseaseName": ["Infant Death"],
            "DiseaseID": ["D0660884"],
            "PubMedIDs": [283930756],  # PubMedId can be int or str
        }
    ),
    pd.DataFrame(
        {
            "Digest": [
                b"\xe1 \xbf\xec\xd6\x1e\xe1F\xbb:La\xf8\xdb\xb97T\xb1\xdb%\xf6*\xbaPXr\xefUh\xdd\x15["
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
                b"\xf8G\xdc\xfe\xaa\xae\x8f\xef\xa9n\x1fn\x97\xddY\x98\xff\xe0se\xd1%K\xad\xae\x92}\x17i\xa2\xee\xbc"
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
