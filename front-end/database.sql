\c genie;

-- DROP TABLE paper_links;

CREATE TABLE paper_links(
  id character varying PRIMARY KEY,
  mesh_id character varying NOT NULL,
  gene_id character varying NOT NULL,
  pmid character varying NOT NULL,
  year smallint NOT NULL,
  citations integer NOT NULL,
  title character varying NOT NULL,
  link character varying NOT NULL
);

CREATE INDEX index_paper_links_on_mesh_id ON paper_links USING btree (mesh_id);
CREATE INDEX index_paper_links_on_gene_id ON paper_links USING btree (gene_id);
CREATE INDEX index_paper_links_on_citations ON paper_links USING btree (citations);


-- DROP TABLE disease_pubs;

CREATE TABLE disease_pubs(
  id character varying NOT NULL,
  year smallint NOT NULL,
  pmid_cum_sum integer NOT NULL,
  citations_cum_sum integer NOT NULL,
  PRIMARY KEY (id, year)
);


-- DROP TABLE gene_pubs;

CREATE TABLE gene_pubs(
  id character varying NOT NULL,
  year smallint NOT NULL,
  pmid_cum_sum integer NOT NULL,
  citations_cum_sum integer NOT NULL,
  PRIMARY KEY (id, year)
);


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
CREATE INDEX index_relationships_on_mesh_id_btree ON relationships USING btree(mesh_id);
CREATE INDEX index_relationships_on_gene_id ON relationships USING GIN(gene_id gin_trgm_ops);
CREATE INDEX index_relationships_on_gene_id_btree ON relationships USING btree(gene_id);
CREATE INDEX index_relationships_on_disease_name ON relationships USING GIN(disease_name gin_trgm_ops);
CREATE INDEX index_relationships_on_disease_name_btree ON relationships USING btree(disease_name);
CREATE INDEX index_relationships_on_gene_name ON relationships USING GIN(gene_name gin_trgm_ops);
CREATE INDEX index_relationships_on_gene_name_btree ON relationships USING btree(gene_name);
CREATE INDEX index_relationships_on_change_recent ON relationships USING btree (change_recent);
CREATE INDEX index_relationships_on_recent_prob_change ON relationships USING btree (recent_prob_change);
CREATE INDEX index_relationships_on_previous_prob ON relationships USING btree (previous_prob);
CREATE INDEX index_relationships_on_num_pubs ON relationships USING btree (num_pubs);
CREATE INDEX index_relationships_on_num_citations ON relationships USING btree (num_citations);


-- DROP TABLE sjr_stats;

CREATE TABLE sjr_stats(
  id character varying NOT NULL,
  year smallint NOT NULL,
  hindex integer NOT NULL,
  sjr integer NOT NULL,
  us_published integer NOT NULL,
  uk_published integer NOT NULL
);


-- DROP TABLE pub_sums;

CREATE TABLE pub_sums(
  id character varying NOT NULL,
  year smallint NOT NULL,
  pmid_sum integer NOT NULL,
  citations_sum integer NOT NULL
);


-- DROP TABLE journal_sums;

CREATE TABLE journal_sums(
  id character varying NOT NULL,
  year smallint NOT NULL,
  journal_sum integer NOT NULL
);


-- DROP TABLE pubmed_ranks;

CREATE TABLE pubmed_ranks(
  id character varying PRIMARY KEY,
  pubmed_rank numeric(16,8) NOT NULL,
  citations integer NOT NULL
);

CREATE INDEX index_pubmed_ranks_on_pubmed_rank ON pubmed_ranks USING btree (pubmed_rank);
CREATE INDEX index_pubmed_ranks_on_citations ON pubmed_ranks USING btree (citations);
