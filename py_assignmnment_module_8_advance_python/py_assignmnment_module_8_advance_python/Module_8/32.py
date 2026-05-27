# 9. SQLite3 and PyMySQL (Database Connectors)

# Write a Python program to create a database and a table using SQLite3.

import sqlite3

# Create and connect database
conn = sqlite3.connect("college.db")

# Create cursor object
cur = conn.cursor()

# Create table
cur.execute("""
CREATE TABLE student (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

print("Database and table created successfully")

# Close connection
conn.close()