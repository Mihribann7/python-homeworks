import sqlite3
import pandas as pd

conn = sqlite3.connect('chinook.db')
df = pd.read_sql_query('SELECT * FROM customers', conn)
print(df.head(10))



conn.close()