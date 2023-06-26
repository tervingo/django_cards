import csv
import sqlite3
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()

# Connect to the existing SQLite database
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Read data from the CSV file and insert into the database
with open('data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row

    for row in csv_reader:
        # Extract data from each row
        question = row[0]
        answer = row[1]
        box = row[2]
        date_created = now


        print("Question is {0}, answer {1}, box {2}, now {3}".format(question, answer, box, date_created))

        # Insert the data into the database
        cursor.execute('INSERT INTO ejercicios_card (question, answer, box, date_created) VALUES (?, ?, ?, ?)',
                       (question, answer, box, date_created))

# Commit the changes and close the connection
conn.commit()
conn.close()
