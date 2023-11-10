from faker import Faker
import psycopg2

import os

# Connect to the local Postgres database
conn = psycopg2.connect(
    host="localhost",
    database="database",
    user="admin",
    password="admin",
)

# Create a cursor object
cur = conn.cursor()

# Generate fake data using the Faker library
fake = Faker()

# create a table if not exists
cur.execute(
    "CREATE TABLE IF NOT EXISTS mytable (id SERIAL PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), phone VARCHAR(255))"
)

# Insert fake data into a table
for i in range(100):
    name = fake.name()
    email = fake.email()
    phone = fake.phone_number()
    cur.execute(
        "INSERT INTO mytable (name, email, phone) VALUES (%s, %s, %s)",
        (name, email, phone),
    )

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
