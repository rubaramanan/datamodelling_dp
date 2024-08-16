from datetime import datetime, timedelta

import pandas as pd
from airflow.decorators import dag, task

from scripts.postgresqlHandler import save_data
from scripts.utils import get_month
import holidays

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
def datedimension():
    @task
    def extract(start_date: str, end_date: str):
        date_range = pd.date_range(start=start_date, end=end_date)

        # Create a DataFrame for the date dimension
        date_dim = pd.DataFrame({
            'Date': date_range,
            'Year': date_range.year,
            'Month': get_month(date_range.month),
            'Day': date_range.day,
            'Quarter': date_range.quarter,
            'Weekday': date_range.day_name(),
            'IsHoliday': 0  # Assuming no holiday data; modify as needed
        })

        us_holidays = holidays.CA(years=date_range.year.unique())

        # Determine if each date is a holiday
        date_dim['IsHoliday'] = date_dim['Date'].isin(us_holidays)

        # Convert boolean to integer (0 = not a holiday, 1 = holiday)
        date_dim['IsHoliday'] = date_dim['IsHoliday'].astype(int)
        # Add a DateKey column (optional: convert to integer format YYYYMMDD)
        date_dim['DateKey'] = date_dim['Date'].dt.strftime('%Y%m%d').astype(int)

        # Rearrange columns if necessary
        return date_dim[['DateKey', 'Date', 'Year', 'Month', 'Day', 'Quarter', 'Weekday', 'IsHoliday']]

    @task
    def load(data):
        save_data(data, 'dimdate')

    extracted_data = extract('1998-01-01', '2024-12-31')
    load(extracted_data)


dsa_dag = datedimension()
