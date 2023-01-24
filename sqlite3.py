
'''import sqlite3

#create a connection
conn = sqlite3.connect('students.db')
# Create a table
c = conn.cursor()
c.execute("""CREATE TABLE students (    
            name TEXT,    
            age INTEGER,    
            height REAL    
    )""")

""" datatypes can be: null, integer, real, text, blob which is a collection of binary data stored as a value in the database. It allows us to store documents, images, and other multimedia files in the database."""

conn.commit()
conn.close()

# to enter one row into our table
c.execute("INSERT INTO students VALUES ('mark', 20, 1.9)")

# Before running the above, the create table line must be commented out.

# to add multiple rows
all_students = [
    ('john', 21, 1.8),
    ('david', 35, 1.7),
    ('michael', 19, 1.83),
]
c.executemany("INSERT INTO students VALUES (?, ?, ?)", all_students)

c.execute("SELECT * FROM students")
print(c.fetchall())


# Using pandas and SQLite
# We will work with a dataframe. A csv file 'population_total.csv'
import pandas as pd

df = pd.read_csv('population_total.csv')

# create an in-memory SQLite database.
from sqlalchemy import create_engine
engine = create_engine('sqlite://', echo=False)

# We can attach the dataframe to a table in our database
# The table doesn't need to be created in advance.
# We will attach df to a table named 'population'
df.to_sql('population', con=engine)

# to see our table we run:
engine.execute("SELECT * FROM population").fetchall()

# to create a sqlite file use:
from sqlalchemy import create_engine    
engine = create_engine("sqlite:///mydb.db")
df.to_sql("population", engine)
    
engine = create_engine("sqlite:///mydb.db")
df.to_sql("population", engine)
engine.execute("SELECT * FROM population").fetchall()
'''
