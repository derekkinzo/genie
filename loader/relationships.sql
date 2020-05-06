CREATE DATABASE genie;

\c genie;
CREATE EXTENSION pg_trgm;

-- DROP TABLE relationships;

CREATE TABLE relationships(
  id character varying PRIMARY KEY,
  p2_prob smallint NOT NULL,
  mesh_id character varying NOT NULL,
  gene_id character varying NOT NULL,
  disease_name character varying NOT NULL,
  gene_name character varying NOT NULL,
  change_recent boolean NOT NULL,
  recent_prob_change smallint NOT NULL,
  previous_prob smallint NOT NULL,
  num_pubs integer NOT NULL,
  num_citations integer NOT NULL
);

CREATE INDEX index_relationships_on_id ON relationships USING GIN(id gin_trgm_ops);
CREATE INDEX index_relationships_on_p2_prob ON relationships USING btree (p2_prob);
CREATE INDEX index_relationships_on_mesh_id ON relationships USING GIN(mesh_id gin_trgm_ops);
CREATE INDEX index_relationships_on_gene_id ON relationships USING GIN(gene_id gin_trgm_ops);
CREATE INDEX index_relationships_on_disease_name ON relationships USING GIN(disease_name gin_trgm_ops);
CREATE INDEX index_relationships_on_gene_name ON relationships USING GIN(gene_name gin_trgm_ops);
CREATE INDEX index_relationships_on_change_recent ON relationships USING btree (change_recent);
CREATE INDEX index_relationships_on_recent_prob_change ON relationships USING btree (recent_prob_change);
CREATE INDEX index_relationships_on_previous_prob ON relationships USING btree (previous_prob);
CREATE INDEX index_relationships_on_num_pubs ON relationships USING btree (num_pubs);
CREATE INDEX index_relationships_on_num_citations ON relationships USING btree (num_citations);
