from datetime import datetime, timedelta

import pandas as pd
from airflow.decorators import dag, task

from scripts.postgresqlHandler import save_data
from scripts.utils import date_key

default_args = {
    'owner': 'Ramanan',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}


@dag(
    default_args=default_args,
    description='dag sending mock data to kafka',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 8, 1),
    catchup=False,
)
def etl():
    @task
    def extract(file: str):
        return pd.read_csv(file)

    @task
    def transform(df):
        print(df)
        df['date'] = df.apply(lambda x: x.datetime.split()[0], axis=1)
        df['time'] = df.apply(lambda x: x.datetime.split()[1], axis=1)

        df['DateKey'] = df.apply(lambda x: date_key(x.date), axis=1)
        df.drop(['datetime', 'date', 'time'], axis=1, inplace=True)
        return df

    @task
    def load(df):
        save_data(df, 'factstockprices')

    extracted_data = extract('/opt/airflow/dags/stocks.csv')
    transformed_data = transform(extracted_data)
    load(transformed_data)


dsa_dag = etl()
