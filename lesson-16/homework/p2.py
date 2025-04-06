import sqlite3
import pandas as pd

df = pd.read_json('iris.json')
print("Shape: ", df.shape)
print("Columns: ", df.columns.tolist())

df = df.apply(lambda col: col.str.lower() if col.dtype == 'object' else col)
print("Columns: ", df.columns.tolist())


print(df.describe())