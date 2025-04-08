import sqlite3
import pandas as pd

conn = sqlite3.connect('chinook.db')
customers = pd.read_sql_query('SELECT * FROM customers', conn)
invoices = pd.read_sql_query('SELECT * FROM invoices', conn)
merged = pd.merge(customers, invoices, on='CustomerId', how='inner')
invoice_counts = merged.groupby('CustomerId').size().reset_index(name='InvoiceCount')

print(invoice_counts.head())
conn.close()

movies = pd.read_csv('movie.csv')
df1 = movies[['director_name', 'color']]
df2 = movies[['director_name', 'num_critic_for_reviews']]
left_join = pd.merge(df1, df2, on='director_name', how='left')

full_outer_join = pd.merge(df1, df2, on='director_name', how='outer')
print("Left Join Rows:", len(left_join))
print("Full Outer Join Rows:", len(full_outer_join))
