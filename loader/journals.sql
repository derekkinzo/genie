CREATE DATABASE genie;

\c genie;
CREATE EXTENSION pg_trgm;

-- DROP TABLE journals;

CREATE TABLE journals(
  id character varying NOT NULL,
  year smallint NOT NULL,
  count smallint NOT NULL,
  PRIMARY KEY(id, year)
);

CREATE INDEX index_journals_on_year ON journals USING btree (year);
CREATE INDEX index_journals_on_count ON journals USING btree (count);
CREATE INDEX index_journals_on_id_gin ON journals USING GIN(id gin_trgm_ops);
