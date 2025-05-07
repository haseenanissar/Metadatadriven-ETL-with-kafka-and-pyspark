from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from kafka import KafkaConsumer
import json
import psycopg2

def consume_kafka_messages():
    consumer = KafkaConsumer(
        'pg_server.sourcedb.public.test_table',
        bootstrap_servers='kafka:9092',
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='etl_group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    conn = psycopg2.connect(database="targetdb", user="postgres", password="password123", host="postgres", port="5432")
    cursor = conn.cursor()

    for msg in consumer:
        data = msg.value
        cursor.execute("INSERT INTO test_table (id, name) VALUES (%s, %s)", (data['id'], data['name']))
        conn.commit()

    conn.close()

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 12),
    'catchup': False
}

dag = DAG('metadata_driven_etl', default_args=default_args, schedule_interval='@hourly')

task = PythonOperator(
    task_id='consume_kafka',
    python_callable=consume_kafka_messages,
    dag=dag
)
