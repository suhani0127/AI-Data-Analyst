import sqlite3
import pandas as pd

df = pd.read_csv("data/Sample - Superstore.csv")

#creating database
conn = sqlite3.connect("store.db")

#storing table
df.to_sql("Sales", conn, if_exists="replace", index = False)

conn.close()

print("Database created succesfully!!")

