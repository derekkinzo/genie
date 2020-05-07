CREATE DATABASE genie;

\c genie;
CREATE EXTENSION pg_trgm;

DROP TABLE paper_links;

CREATE TABLE paper_links(
  id character varying PRIMARY KEY,
  mesh_id character varying NOT NULL,
  gene_id character varying NOT NULL,
  pmid integer NOT NULL,
  year smallint NOT NULL,
  citations integer NOT NULL,
  link character varying NOT NULL
);

CREATE INDEX index_paper_links_on_mesh_id ON paper_links USING btree (mesh_id);
CREATE INDEX index_paper_links_on_gene_id ON paper_links USING btree (gene_id);
CREATE INDEX index_paper_links_on_citations ON paper_links USING btree (citations);
