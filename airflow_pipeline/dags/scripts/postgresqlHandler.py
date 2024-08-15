import psycopg2


def save_data(data, table):
    try:
        # Connect to PostgreSQL database
        conn = psycopg2.connect(
            dbname="ramanan_db",
            user="airflow",
            password="airflow",
            host="192.168.2.79",
            port="5432"
        )
        cursor = conn.cursor()

        # Create insert statement dynamically
        cols = ",".join(list(data.columns))
        for i, row in data.iterrows():
            sql = f"INSERT INTO {table} ({cols}) VALUES ({'%s, ' * (len(row) - 1)}%s)"
            cursor.execute(sql, tuple(row))

        # Commit the transaction and close the connection
        conn.commit()
        cursor.close()
        conn.close()
        print(f"Data successfully stored in the table '{table}' in PostgreSQL")

    except Exception as e:
        print(f"An error occurred: {e}")
    # engine = create_engine('postgresql+psycopg2://ramanan:S3cret@192.168.2.79:5433/ramanan_db')
    #
    # data.to_sql(table, engine, if_exists='replace', index=False)
    #
    # print("data stored in postgresql")
