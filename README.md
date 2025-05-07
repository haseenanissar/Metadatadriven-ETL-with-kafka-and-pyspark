# Metadatadriven-ETL-with-kafka-and-pyspark
# 🧠 Metadata-Driven ETL Pipeline (PostgreSQL, SQL Server ➜ MySQL, Snowflake)

## 📌 Overview

This project implements a **metadata-driven ETL pipeline** that:
- Extracts data from multiple **source databases** (PostgreSQL, SQL Server)
- Uses **Debezium + Kafka** for real-time CDC (Change Data Capture)
- Applies **transformation logic** using metadata rules stored in PostgreSQL
- Loads data into **destination databases** (MySQL, Snowflake)
- Enables reporting and visualization with **Power BI**
- Is fully containerized using **Docker Compose**

---

## 🛠️ Tech Stack

| Layer            | Tools / Technologies                          |
|------------------|-----------------------------------------------|
| 🗃️ Source DBs     | PostgreSQL, SQL Server                        |
| 🔄 CDC Engine     | Debezium                                      |
| 📡 Messaging      | Apache Kafka + Zookeeper                      |
| 🧠 Metadata DB    | PostgreSQL (fraud rules / transformation logic) |
| 🔧 Transformation | PySpark                                       |
| 📥 Destinations   | MySQL, Snowflake                              |
| 🎯 Orchestration  | Apache Airflow                                |
| 📊 BI Tool        | Power BI (connects to MySQL/Snowflake)        |
| 📦 Containerization| Docker + Docker Compose                       |

---

## 📁 Project Structure

```bash
metadata-etl-pipeline/
├── docker-compose.yml
├── kafka/
│   └── connect/
│       └── postgres-connector.json
├── metadata-db/
│   └── init/
│       └── init.sql
├── spark/
│   └── etl_job.py
├── airflow/
│   └── dags/
│       └── metadata_etl_dag.py
├── envs/
│   └── snowflake.env
└── README.md



 How It Works
1. Metadata Table in PostgreSQL
Stores transformation rules:

sql
Copy
Edit
CREATE TABLE etl_rules (
  source_db VARCHAR,
  table_name VARCHAR,
  column_name VARCHAR,
  transformation_rule TEXT,
  target_db VARCHAR,
  target_table VARCHAR
);
2. CDC via Kafka + Debezium
Debezium connectors capture changes from PostgreSQL and SQL Server and publish them to Kafka topics.

3. Transformation via PySpark
Spark reads Kafka streams and applies transformations based on the metadata rules from PostgreSQL.

4. Load to Destinations
Transformed data is loaded into:

MySQL for dashboarding

Snowflake for analytics and data warehousing

5. Airflow DAG
Orchestrates the ETL job and monitors executions.

6. Power BI
Connects directly to MySQL and Snowflake to build dashboards.
