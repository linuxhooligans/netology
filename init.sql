CREATE DATABASE candydendydb;
CREATE USER candydendyuser WITH PASSWORD 'SuperSweetBuns2022';
GRANT ALL PRIVILEGES ON DATABASE candydendydb TO candydendyuser;
\connect candydendydb;
CREATE SCHEMA candydendyschema;
GRANT ALL ON ALL FUNCTIONS IN SCHEMA candydendyschema to candydendyuser;
GRANT ALL ON ALL SEQUENCES IN SCHEMA candydendyschema to candydendyuser;
GRANT ALL ON ALL TABLES IN SCHEMA candydendyschema to candydendyuser;
ALTER SCHEMA candydendyschema OWNER TO candydendyuser;
