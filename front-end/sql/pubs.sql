CREATE DATABASE genie;

\c genie;
CREATE EXTENSION pg_trgm;

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
