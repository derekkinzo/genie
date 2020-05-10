CREATE DATABASE genie;

\c genie;
CREATE EXTENSION pg_trgm;

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
