"""Module containing definitions of tables repository tables."""
from collections import namedtuple
from sqlalchemy import MetaData, Table, Column, Integer, Float, String

RepoProperties = namedtuple("RepoProperties", "tablename pkey table")
"""General properties of a given repository."""

CTD_PKEY = "digest"
"""CTD table primary key."""
CTD_TABLE_NAME = "ctd"
"""Name of ctd source table."""
CTD_DAO_TABLE = Table(
    CTD_TABLE_NAME,
    MetaData(),
    # No primary key allows duplicate records
    Column("digest", String, primary_key=False, nullable=False),
    Column("genesymbol", String),
    Column("geneid", Integer, nullable=False),
    Column("diseasename", String),
    Column("diseaseid", String, nullable=False),
    Column("pmids", String, nullable=False),
)
"""CTD DAO Repository Schema."""
CTD_PROPTY = RepoProperties(
    tablename=CTD_TABLE_NAME, pkey=CTD_PKEY, table=CTD_DAO_TABLE
)


PUBMED_TABLE_NAME = "pubmed"
"""PUBMED table primary key."""
PUBMED_PKEY = "pmid"
"""Name of pubmed source table."""
PUBMED_DAO_TABLE = Table(
    PUBMED_TABLE_NAME,
    MetaData(),
    # No primary key allows duplicate records
    Column("pmid", Integer, primary_key=False, nullable=False),
    Column("date_completed", String),
    Column("pub_model", String),
    Column("title", String),
    Column("iso_abbreviation", String),
    Column("article_title", String),
    Column("abstract", String),
    Column("authors", String),
    Column("language", String),
    Column("chemicals", String),
    Column("mesh_list", String),
)
"""PUBMED DAO Repository Schema."""
PUBMED_PROPTY = RepoProperties(
    tablename=PUBMED_TABLE_NAME, pkey=PUBMED_PKEY, table=PUBMED_DAO_TABLE
)

CLSFR_PKEY = "digest"
"""Classifier table primary key."""
CLSFR_TABLE_NAME = "classifier"
"""Classifier table name."""
CLSFR_TABLE_NAME = "classifier"
"""Name of geniepy classifier output table."""
CLSFR_DAO_TABLE = Table(
    CLSFR_TABLE_NAME,
    MetaData(),
    # No primary key allows duplicate records
    Column("digest", String, primary_key=False, nullable=False),
    Column("pub_score", Float, nullable=False),
    Column("ct_score", Float, nullable=False),
)
"""Classifier Output DAO Repository Schema."""
CLSFR_PROPTY = RepoProperties(
    tablename=CLSFR_TABLE_NAME, pkey=CLSFR_PKEY, table=CLSFR_DAO_TABLE
)


FEATURES_PKEY = "gene_id"
"""Features table primary key."""
FEATURES_TABLE_NAME = "scoring_data"
"""Features table name."""
FEATURES_DAO_TABLE = None
"""Features Output DAO Repository Schema."""
FEATURES_PROPTY = RepoProperties(
    tablename=FEATURES_TABLE_NAME, pkey=FEATURES_PKEY, table=FEATURES_DAO_TABLE
)

SCORES_PKEY = "gene_id"
"""Scoring table primary key."""
SCORES_TABLE_NAME = "scores"
"""Scoring table name."""
SCORES_DAO_TABLE = None
"""Scoring Output DAO Repository Schema."""
SCORES_PROPTY = RepoProperties(
    tablename=SCORES_TABLE_NAME, pkey=SCORES_PKEY, table=SCORES_DAO_TABLE
)
