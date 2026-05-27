# 9. SQLite3 and PyMySQL (Database Connectors)

# Write a Python program to connect to an SQLite3 database, create a table, insert data, and fetch data.

import sqlite3

# Connect to database
conn = sqlite3.connect("student.db")

# Create cursor object
cur = conn.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

# Insert data
cur.execute("INSERT INTO student (name, age) VALUES (?, ?)", ("Jinal", 21))

# Save changes
conn.commit()

# Fetch data
cur.execute("SELECT * FROM student")

data = cur.fetchall()

# Display data
for row in data:
    print(row)

# Close connection
conn.close()