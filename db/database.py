import sqlite3

def store_data_to_sqlite(df, table_name):
    conn = sqlite3.connect('db/economy_data.db')
    df.to_sql(table_name, conn, if_exists='append', index=False)
    conn.close()
