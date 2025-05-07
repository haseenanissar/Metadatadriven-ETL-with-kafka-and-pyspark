import json
import psycopg2
import pymysql
import pyodbc
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="kafka:9092",
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

metadata_conn = psycopg2.connect(
    dbname="metadata_db",
    user="user",
    password="password",
    host="postgres"
)
cursor = metadata_conn.cursor()

cursor.execute("SELECT * FROM etl_metadata")
metadata_rows = cursor.fetchall()

for row in metadata_rows:
    source_db_type, source_db_host, source_db_port, source_db_user, source_db_password, source_db_name, source_table, kafka_topic = row[1:9]

    if source_db_type == "postgresql":
        conn = psycopg2.connect(
            dbname=source_db_name, user=source_db_user, password=source_db_password, host=source_db_host, port=source_db_port
        )
    elif source_db_type == "mysql":
        conn = pymysql.connect(
            host=source_db_host, user=source_db_user, password=source_db_password, database=source_db_name, port=source_db_port
        )
    elif source_db_type == "sqlserver":
        conn = pyodbc.connect(f"DRIVER={{SQL Server}};SERVER={source_db_host};DATABASE={source_db_name};UID={source_db_user};PWD={source_db_password}")

    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {source_table}")
    rows = cursor.fetchall()

    for row in rows:
        producer.send(kafka_topic, value=dict(row))

producer.close()
