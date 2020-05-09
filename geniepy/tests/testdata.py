"""Module with data used in tests."""
# flake8: noqa
# pylint: skip-file
import pandas as pd


PUBMED_INVALID_SCHEMA = [
    pd.DataFrame(
        {
            # Missing required column
            "date_completed": ["--"],
            "pub_model": ["Print-Electronic"],
            "title": ["Biochemia medica"],
            "iso_abbreviation": ["Biochem Med (Zagreb)"],
            "article_title": [
                "High anion gap metabolic acidosis caused by D-lactate: mind the time of blood collection."  # NOQA
            ],
            "abstract": [
                "D-lactic acidosis is an uncommon cause of high anion gap acidosis."
            ],
            "authors": ["Weemaes, Matthias, Hiele, Martin, Vermeersch, Pieter"],
            "language": ["eng"],
            "chemicals": [""],
            "mesh_list": [""],
        }
    ),
    pd.DataFrame(
        {
            "pmid": 31839729,
            "not column": [""],  # Invalid Column
            "pub_model": ["Print-Electronic"],
            "title": ["Biochemia medica"],
            "iso_abbreviation": ["Biochem Med (Zagreb)"],
            "article_title": [
                "Unexpected abnormal coagulation test results in a 2-year-old child: A case report."
            ],
            "abstract": [
                "Rejection of the sample with repeated blood withdrawal is always an unwanted consequence of sample nonconformity and preanalytical errors, especially in the most vulnerable population - children. Here is presented a case with unexpected abnormal coagulation test results in a 2-year-old child with no previously documented coagulation disorder. Child is planned for tympanostomy tubes removal under the anaesthesia driven procedure, and preoperative coagulation tests revealed prolonged prothrombin time, activated partial thromboplastin time and thrombin time, with fibrinogen and antithrombin within reference intervals. From the anamnestic and clinical data, congenital coagulation disorder was excluded, and with further investigation, sample mismatch, clot presence and accidental ingestion of oral anticoagulant, heparin contamination or vitamin K deficiency were excluded too. Due to suspected EDTA carryover during blood sampling another sample was taken the same day and all tests were performed again. The results for all tests were within reference intervals confirming EDTA effect on falsely prolongation of the coagulation times in the first sample. This case can serve as alert to avoid unnecessary loss in terms of blood withdrawal repetitions and discomfort of the patients and their relatives, tests repeating, prolonging medical procedures, and probably delaying diagnosis or proper medical treatment. It is the responsibility of the laboratory specialists to continuously educate laboratory staff and other phlebotomists on the correct blood collection as well as on its importance for the patient's safety."
            ],
            "authors": [
                "Banković Radovanović, Patricija, Živković Mikulčić, Tanja, Simović Medica, Jasmina"
            ],
            "language": ["eng"],
            "chemicals": [""],
            "mesh_list": [""],
        }
    ),
]


PUBMED_INVALID_DF = [
    pd.DataFrame(
        {
            "pmid": ["31839728"],  # pmid as string
            "date_completed": ["--"],
            "pub_model": ["Print-Electronic"],
            "title": ["Biochemia medica"],
            "iso_abbreviation": ["Biochem Med (Zagreb)"],
            "article_title": [
                "High anion gap metabolic acidosis caused by D-lactate: mind the time of blood collection."
            ],
            "abstract": [
                "D-lactic acidosis is an uncommon cause of high anion gap acidosis."
            ],
            "authors": ["Weemaes, Matthias, Hiele, Martin, Vermeersch, Pieter"],
            "language": ["eng"],
            "chemicals": [""],
            "mesh_list": [""],
        }
    ),
    pd.DataFrame(
        {
            "pmid": 31839729,
            # missing column
            "pub_model": ["Print-Electronic"],
            "title": ["Biochemia medica"],
            "iso_abbreviation": ["Biochem Med (Zagreb)"],
            "article_title": [
                "Unexpected abnormal coagulation test results in a 2-year-old child: A case report."
            ],
            "abstract": [
                "Rejection of the sample with repeated blood withdrawal is always an unwanted consequence of sample nonconformity and preanalytical errors, especially in the most vulnerable population - children. Here is presented a case with unexpected abnormal coagulation test results in a 2-year-old child with no previously documented coagulation disorder. Child is planned for tympanostomy tubes removal under the anaesthesia driven procedure, and preoperative coagulation tests revealed prolonged prothrombin time, activated partial thromboplastin time and thrombin time, with fibrinogen and antithrombin within reference intervals. From the anamnestic and clinical data, congenital coagulation disorder was excluded, and with further investigation, sample mismatch, clot presence and accidental ingestion of oral anticoagulant, heparin contamination or vitamin K deficiency were excluded too. Due to suspected EDTA carryover during blood sampling another sample was taken the same day and all tests were performed again. The results for all tests were within reference intervals confirming EDTA effect on falsely prolongation of the coagulation times in the first sample. This case can serve as alert to avoid unnecessary loss in terms of blood withdrawal repetitions and discomfort of the patients and their relatives, tests repeating, prolonging medical procedures, and probably delaying diagnosis or proper medical treatment. It is the responsibility of the laboratory specialists to continuously educate laboratory staff and other phlebotomists on the correct blood collection as well as on its importance for the patient's safety."
            ],
            "authors": [
                "Banković Radovanović, Patricija, Živković Mikulčić, Tanja, Simović Medica, Jasmina"
            ],
            "language": ["eng"],
            "chemicals": [""],
            "mesh_list": [""],
        }
    ),
    pd.DataFrame(
        {
            "pmid": 31839730,
            "date_completed": ["--"],
            "pub_model": ["Print-Electronic"],
            "title": ["Narrative inquiry : NI"],
            "iso_abbreviation": ["Narrat Inq"],
            "article_title": [
                "Narrative Assessments with First Grade Spanish-English Emergent Bilinguals: Spontaneous versus Retell Conditions."
            ],
            "abstract": [
                "This study used qualitative analyses to investigate similarities and differences in narrative production across two task conditions for four first grade Spanish-English emergent bilingual children. Task conditions were spontaneous story generation and retelling using the same story. Spanish stories from two children were compared on the basis of similarity in vocabulary, while English stories from two children were compared on the basis of similarity in overall discourse skills. Results show that when the total number of words used was similar across English narratives, the retell included more different words and higher quality story structure than the spontaneous story. When overall discourse scores in the Spanish examples were similar, the spontaneous story required more words than the retell, but also included more central events and greater detail. Yet, the retell included more advanced narrative components. This study contributes to our understanding of narrative skills in young Spanish-English bilinguals across task conditions."
            ],
            "authors": ["Lucero, Audrey, Uchikoshi, Yuuko"],
            "language": ["eng"],
            "chemicals": [""],
            "mesh_list": [""],
            "other col": [""],  # Extra column
        }
    ),
    pd.DataFrame(
        {
            "pmid": 31839731,
            "date_completed": ["--"],
            "pub_model": ["Print"],
            "title": ["Acta ortopedica brasileira"],
            "iso_abbreviation": ["Acta Ortop Bras"],
            "article_title": [
                "CHRONIC MONTEGGIA FRACTURE-DISLOCATION IN CHILDREN SURGICAL STRATEGY AND RESULTS."
            ],
            "abstract": [
                "To report surgical techniques and results in the treatment of chronic Monteggia fracture-dislocation in children."
            ],
            "authors": [
                "Soni, Jamil Faissal, Valenza, Weverley Rubele, Matsunaga, Carolina Umeta, Costa, Anna Carolina Pavelec, Faria, Fernando Ferraz"
            ],
            "language": ["eng"],
            # Missing column
            "mesh_list": [""],
        }
    ),
    pd.DataFrame(
        {
            "pmid": 31839732,
            "date_completed": ["--"],
            "pub_model": ["Print"],
            "title": ["Acta ortopedica brasileira"],
            # Missing Column
            # Missing Column
            "abstract": [
                "To evaluate the efficacy of platelet-rich plasma (PRP) and tranexamic acid (TXA) applied in total knee arthroplasty."
            ],
            "authors": [
                "Guerreiro, João Paulo Fernandes, Lima, Diogenes Rodrigues, Bordignon, Glaucia, Danieli, Marcus Vinicius, Queiroz, Alexandre Oliveira, Cataneo, Daniele Cristina"
            ],
            "language": ["eng"],
            "chemicals": [""],
            "mesh_list": [""],
        }
    ),
]
"""Array of invalid PubMed dataframes."""


PUBMED_VALID_DF = [
    pd.DataFrame(
        {
            "pmid": 31839728,
            "date_completed": ["--"],
            "pub_model": ["Print-Electronic"],
            "title": ["Biochemia medica"],
            "iso_abbreviation": ["Biochem Med (Zagreb)"],
            "article_title": [
                "High anion gap metabolic acidosis caused by D-lactate: mind the time of blood collection."
            ],
            "abstract": [
                "D-lactic acidosis is an uncommon cause of high anion gap acidosis."
            ],
            "authors": ["Weemaes, Matthias, Hiele, Martin, Vermeersch, Pieter"],
            "language": ["eng"],
            "chemicals": [""],
            "mesh_list": [""],
            "issn": ["1234-5678"],
            "issn_type": ["Print"], 
            "citation_count": 0,
            "citation_pmid": [""],
        }
    ),
    pd.DataFrame(
        {
            "pmid": 31839729,
            "date_completed": ["--"],
            "pub_model": ["Print-Electronic"],
            "title": ["Biochemia medica"],
            "iso_abbreviation": ["Biochem Med (Zagreb)"],
            "article_title": [
                "Unexpected abnormal coagulation test results in a 2-year-old child: A case report."
            ],
            "abstract": [
                "Rejection of the sample with repeated blood withdrawal is always an unwanted consequence of sample nonconformity and preanalytical errors, especially in the most vulnerable population - children. Here is presented a case with unexpected abnormal coagulation test results in a 2-year-old child with no previously documented coagulation disorder. Child is planned for tympanostomy tubes removal under the anaesthesia driven procedure, and preoperative coagulation tests revealed prolonged prothrombin time, activated partial thromboplastin time and thrombin time, with fibrinogen and antithrombin within reference intervals. From the anamnestic and clinical data, congenital coagulation disorder was excluded, and with further investigation, sample mismatch, clot presence and accidental ingestion of oral anticoagulant, heparin contamination or vitamin K deficiency were excluded too. Due to suspected EDTA carryover during blood sampling another sample was taken the same day and all tests were performed again. The results for all tests were within reference intervals confirming EDTA effect on falsely prolongation of the coagulation times in the first sample. This case can serve as alert to avoid unnecessary loss in terms of blood withdrawal repetitions and discomfort of the patients and their relatives, tests repeating, prolonging medical procedures, and probably delaying diagnosis or proper medical treatment. It is the responsibility of the laboratory specialists to continuously educate laboratory staff and other phlebotomists on the correct blood collection as well as on its importance for the patient's safety."
            ],
            "authors": [
                "Banković Radovanović, Patricija, Živković Mikulčić, Tanja, Simović Medica, Jasmina"
            ],
            "language": ["eng"],
            "chemicals": [""],
            "mesh_list": [""],
            "issn": ["1234-5678"],
            "issn_type": ["Print"], 
            "citation_count": 0,
            "citation_pmid": [""],            
        }
    ),
    pd.DataFrame(
        {
            "pmid": 31839730,
            "date_completed": ["--"],
            "pub_model": ["Print-Electronic"],
            "title": ["Narrative inquiry : NI"],
            "iso_abbreviation": ["Narrat Inq"],
            "article_title": [
                "Narrative Assessments with First Grade Spanish-English Emergent Bilinguals: Spontaneous versus Retell Conditions."
            ],
            "abstract": [
                "This study used qualitative analyses to investigate similarities and differences in narrative production across two task conditions for four first grade Spanish-English emergent bilingual children. Task conditions were spontaneous story generation and retelling using the same story. Spanish stories from two children were compared on the basis of similarity in vocabulary, while English stories from two children were compared on the basis of similarity in overall discourse skills. Results show that when the total number of words used was similar across English narratives, the retell included more different words and higher quality story structure than the spontaneous story. When overall discourse scores in the Spanish examples were similar, the spontaneous story required more words than the retell, but also included more central events and greater detail. Yet, the retell included more advanced narrative components. This study contributes to our understanding of narrative skills in young Spanish-English bilinguals across task conditions."
            ],
            "authors": ["Lucero, Audrey, Uchikoshi, Yuuko"],
            "language": ["eng"],
            "chemicals": [""],
            "mesh_list": [""],
            "issn": ["1234-5678"],
            "issn_type": ["Print"], 
            "citation_count": 0,
            "citation_pmid": [""],            
        }
    ),
    pd.DataFrame(
        {
            "pmid": 31839731,
            "date_completed": ["--"],
            "pub_model": ["Print"],
            "title": ["Acta ortopedica brasileira"],
            "iso_abbreviation": ["Acta Ortop Bras"],
            "article_title": [
                "CHRONIC MONTEGGIA FRACTURE-DISLOCATION IN CHILDREN SURGICAL STRATEGY AND RESULTS."
            ],
            "abstract": [
                "To report surgical techniques and results in the treatment of chronic Monteggia fracture-dislocation in children."
            ],
            "authors": [
                "Soni, Jamil Faissal, Valenza, Weverley Rubele, Matsunaga, Carolina Umeta, Costa, Anna Carolina Pavelec, Faria, Fernando Ferraz"
            ],
            "language": ["eng"],
            "chemicals": [""],
            "mesh_list": [""],
            "issn": ["1234-5678"],
            "issn_type": ["Print"], 
            "citation_count": 0,
            "citation_pmid": [""],            
        }
    ),
    pd.DataFrame(
        {
            "pmid": 31839732,
            "date_completed": ["--"],
            "pub_model": ["Print"],
            "title": ["Acta ortopedica brasileira"],
            "iso_abbreviation": ["Acta Ortop Bras"],
            "article_title": [
                "PLATELET-RICH PLASMA (PRP) AND TRANEXAMIC ACID (TXA) APPLIED IN TOTAL KNEE ARTHROPLASTY."
            ],
            "abstract": [
                "To evaluate the efficacy of platelet-rich plasma (PRP) and tranexamic acid (TXA) applied in total knee arthroplasty."
            ],
            "authors": [
                "Guerreiro, João Paulo Fernandes, Lima, Diogenes Rodrigues, Bordignon, Glaucia, Danieli, Marcus Vinicius, Queiroz, Alexandre Oliveira, Cataneo, Daniele Cristina"
            ],
            "language": ["eng"],
            "chemicals": [""],
            "mesh_list": [""],
            "issn": ["1234-5678"],
            "issn_type": ["Print"], 
            "citation_count": 0,
            "citation_pmid": [""],            
        }
    ),
]
"""Array of valid PubMed dataframes."""

CTD_INVALID_SCHEMA = [
    pd.DataFrame(
        {
            # Missing Digest required field
            "genesymbol": ["11-BETA-HSD3"],
            "geneid": [100174880],
            "diseasename": ["Abnormalities, Drug-Induced"],
            "diseaseid": ["D000014"],
            "pmids": ["22659286"],
        }
    ),
    pd.DataFrame(
        {
            "OtherField": [22659286],  # Non-existent schema column
            "digest": [22659286],
            "genesymbol": ["11-BETA-HSD3"],
            "geneid": [100174880],
            "diseasename": ["Abnormalities, Drug-Induced"],
            "diseaseid": ["D000014"],
            "pmids": ["22659286"],
        }
    ),
    pd.DataFrame(
        {
            "digest": [22659286],
            "genesymbol": ["11-BETA-HSD3"],
            # Missing required GeneID
            "diseasename": ["Abnormalities, Drug-Induced"],
            "diseaseid": ["D000014"],
            "pmids": ["22659286"],
        }
    ),
    pd.DataFrame(
        {
            "digest": [22659286],
            "genesymbol": ["11-BETA-HSD3"],
            "geneid": [100174880],
            "diseasename": ["Abnormalities, Drug-Induced"],
            # Missing required DiseaseID
            "pmids": ["22659286"],
        }
    ),
    pd.DataFrame(
        {
            "digest": [22659286],
            "genesymbol": ["11-BETA-HSD3"],
            "geneid": [100174880],
            "diseasename": ["Abnormalities, Drug-Induced"],
            "diseaseid": ["D000014"],
            # Missing required PubMed
        }
    ),
]
"""Invalid SCHEMA record."""

CTD_INVALID_DF = [
    None,
    pd.DataFrame({"invalid": [1, 2]}),
    pd.DataFrame(
        {
            "digest": [22659286],
            "genesymbol": ["11-BETA-HSD3"],
            "geneid": ["A100174880"],  # Should be Int
            "diseasename": ["Abnormalities, Drug-Induced"],
            "diseaseid": ["D000014"],
            "pmids": ["22659286"],
        }
    ),
    pd.DataFrame(
        {
            "digest": [22659286],
            "genesymbol": ["11-BETA-HSD3"],
            "geneid": [100174880.0],  # Should be Int
            "diseasename": ["Abnormalities, Drug-Induced"],
            "diseaseid": ["D000014"],
            "pmids": ["22659286"],
        }
    ),
    pd.DataFrame(
        {
            "digest": [22659286],
            "genesymbol": ["11-BETA-HSD3"],
            "geneid": [100174880],
            "diseasename": ["Abnormalities, Drug-Induced"],
            "diseaseid": ["MESH:D000014"],  # Should not have "MESH:"
            "pmids": ["22659286"],
        }
    ),
] + CTD_INVALID_SCHEMA
"""Array of invalid CTD DataFrames because violate parser rules."""


CTD_VALID_DF = [
    pd.DataFrame(
        {
            "digest": [
                "b3834d9281286247e377c5700e9689c3660412df24fa0a4921c6e3c213d616aa"
            ],
            "genesymbol": ["11-BETA-HSD3"],
            "geneid": [10174880],
            "diseasename": ["Abnormalities, Drug-Induced"],
            "diseaseid": ["D000014"],
            "pmids": ["22659286"],
        }
    ),
    pd.DataFrame(
        {
            "digest": [
                "e96cc1eb2423dad1fd6f4f341574fbb7fff0479a3339c9e2e4f814f2d970e3f00"
            ],
            "genesymbol": ["1-SF3"],
            "geneid": [1000494280],
            "diseasename": ["Infant Death"],
            "diseaseid": ["D0660884"],
            "pmids": ["283930756"],
        }
    ),
    pd.DataFrame(
        {
            "digest": [
                "e120bfecd61ee146bb3a4c61f8dbb93754b1db25f62aba505872ef5568dd155b"
            ],
            "genesymbol": ["11-BETA-HSD3"],
            "geneid": [100174880],
            "diseasename": ["Abnormalities, Drug-Induced"],
            "diseaseid": ["D000014"],
            "pmids": ["22659286"],
        }
    ),
    pd.DataFrame(
        {
            "digest": [
                "f847dcfeaaae8fefa96e1f6e97dd5998ffe07365d1254badae927d1769a2eebc"
            ],
            "genesymbol": ["A1BG3"],
            "geneid": [1],
            "diseasename": ["Muscle Weaknessd"],
            "diseaseid": ["D0189084"],
            "pmids": ["3515563|54800|62135|63766|6511338|7995496"],
        }
    ),
]
"""Array of valid CTD DataFrames."""

CLSFR_VALID_DF = [
    pd.DataFrame(
        {
            "digest": [
                "b3834d9281286247e377c5700e9689c3660412df24fa0a4921c6e3c213d616aa"
            ],
            "pub_score": [0.8],
            "ct_score": [0.7],
        }
    ),
    pd.DataFrame(
        {
            "digest": [
                "e96cc1eb2423dad1fd6f4f341574fbb7fff0479a3339c9e2e4f814f2d970e3f00"
            ],
            "pub_score": [0.8],
            "ct_score": [0.7],
        }
    ),
    pd.DataFrame(
        {
            "digest": [
                "e96cc1eb2423dad1fd6f4f341574fbb7fff0479a3339c9e2e4f814f2d970e3f00"
            ],
            "pub_score": [0.8],
            "ct_score": [0.7],
        }
    ),
]
"""Array of valid classifier dataframes."""


CLSFR_INVALID_DF = [
    pd.DataFrame(
        {
            "digest": [
                "b3834d9281286247e377c5700e9689c3660412df24fa0a4921c6e3c213d616aa"
            ],
            "pub_score": ["1.2"],  # GeneID should be float
            "ct_score": [0.7],
        }
    ),
    pd.DataFrame(
        {
            "digest": [
                "b3834d9281286247e377c5700e9689c3660412df24fa0a4921c6e3c213d616aa"
            ],
            # Missing pub_score
            "ct_score": [0.7],
        }
    ),
    pd.DataFrame(
        {
            "digest": [
                "e96cc1eb2423dad1fd6f4f341574fbb7fff0479a3339c9e2e4f814f2d970e3f00"
            ],
            "pub_score": [0.8],
            "ct_score": ["0.75"],  # Should be float
        }
    ),
]
"""Array of invalid classifier dataframes."""


CLSFR_INVALID_SCHEMA = [
    pd.DataFrame(
        {
            "digest": [
                "b3834d9281286247e377c5700e9689c3660412df24fa0a4921c6e3c213d616aa"
            ],
            # Missing GeneID
            "ct_score": [0.7],
        }
    ),
    pd.DataFrame(
        {
            "digest": [
                "e96cc1eb2423dad1fd6f4f341574fbb7fff0479a3339c9e2e4f814f2d970e3f00"
            ],
            "pub_score": [0.8],
            "ct_score": [0.7],
            "newcol": "newcol",
        }
    ),
    pd.DataFrame(
        {
            # missing digest
            "pub_score": [0.8],
            "ct_score": [0.7],
        }
    ),
    pd.DataFrame(
        {
            "digest": [
                "e96cc1eb2423dad1fd6f4f341574fbb7fff0479a3339c9e2e4f814f2d970e3f00"
            ],
            "pub_score": [0.8],
            # Missing DiseaseID
        }
    ),
]
"""Array of valid classifier SCHEMA table schema."""
