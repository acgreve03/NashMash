import sqlite3
import pandas as pd

# Connect to your database
conn = sqlite3.connect("songs.db")

# Query your data
df = pd.read_sql_query("SELECT * FROM songs WHERE artist = 'Nicki Minaj' LIMIT 10;", conn)

# Display the results
print(df)