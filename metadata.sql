-- Create the metadata database (Run this in your DBMS)
CREATE DATABASE metadata_db;

-- Use the metadata database (For postgres)
USE metadata_db;
--Source Metadata Table
CREATE TABLE metadata_source (
    id SERIAL PRIMARY KEY,
    source_db_type VARCHAR(50),  -- PostgreSQL, MySQL, SQL Server
    source_db_host VARCHAR(255),
    source_db_port INTEGER,
    source_db_name VARCHAR(255),
    source_table_name VARCHAR(255),
    source_column_name VARCHAR(255),
    transformation_rule VARCHAR(255)
);

--Target Metadata Table
CREATE TABLE metadata_target (
    id SERIAL PRIMARY KEY,
    target_db_type VARCHAR(50),  -- Snowflake, PostgreSQL, MySQL
    target_db_host VARCHAR(255),
    target_db_port INTEGER,
    target_db_name VARCHAR(255),
    target_table_name VARCHAR(255),
    target_column_name VARCHAR(255)
);


-- Transformation Metadata Table
CREATE TABLE metadata_transformations (
    id SERIAL PRIMARY KEY,
    source_column_name VARCHAR(255),
    transformation_rule VARCHAR(255)  -- e.g., "uppercase", "mask_email", "convert_date"
);
