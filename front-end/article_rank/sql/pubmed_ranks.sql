CREATE DATABASE pubmed_ranks;

\c genie;
CREATE EXTENSION pg_trgm;

DROP TABLE pubmed_ranks;

CREATE TABLE pubmed_ranks(
  id character varying PRIMARY KEY,
  pubmed_rank numeric(16,8) NOT NULL,
  citations integer NOT NULL
);

CREATE INDEX index_pubmed_ranks_on_pubmed_rank ON pubmed_ranks USING btree (pubmed_rank);
CREATE INDEX index_pubmed_ranks_on_citations ON pubmed_ranks USING btree (citations);
