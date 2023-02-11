# Writing to a text file
with open("example.txt", "w") as file:
    file.write("Hello World")

# Reading from a text file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

import csv

# Writing to a CSV file
with open("example.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Country"])
    writer.writerow(["John Doe", 32, "USA"])
# Reading from a CSV file
with open("example.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


import requests
from bs4 import BeautifulSoup

# Make a request to a website
url = "https://www.example.com"
response = requests.get(url)
# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")
# Extract the data
title = soup.title.text
print(title)


import smtplib

# Connect to the email server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.login("your_email_address@gmail.com", "your_email_password")
# Send the email
from_address = "your_email_address@gmail.com"
to_address = "recipient_email_address@gmail.com"
subject = "Automated Email from Python"
body = "This is an automated email sent from Python."
message = f"Subject: {subject}\n\n{body}"
server.sendmail(from_address, to_address, message)
# Disconnect from the email server
server.quit()

import os
# Rename all files in a directory
directory = "example_directory"
for filename in os.listdir(directory):
    old_file = os.path.join(directory, filename)
    new_file = os.path.join(directory, filename.replace(" ", "_"))
    os.rename(old_file, new_file)


from PIL import Image

# Open an image
image = Image.open("example.jpg")
# Resize the image
image = image.resize((400, 300))
# Save the resized image
image.save("resized_example.jpg")
# Convert the image to a different format
image.save("converted_example.png")


import shutil
# Make a backup copy of a directory
src_directory = "example_directory"
dst_directory = "example_directory_backup"
shutil.copytree(src_directory, dst_directory)


import pandas as pd
import matplotlib.pyplot as plt

# Load data into a Pandas DataFrame
data = pd.read_csv("example_data.csv")
# Plot the data
plt.plot(data["Year"], data["Sales"])
plt.xlabel("Year")
plt.ylabel("Sales")
plt.title("Annual Sales")
plt.show()


import unittest
# Define a test case
class TestExample(unittest.TestCase):
    def test_example(self):
        result = 1 + 1
        self.assertEqual(result, 2)
# Run the test case
if __name__ == "__main__":
    unittest.main()


import sqlite3
# Connect to a SQLite database
connection = sqlite3.connect("example.db")
cursor = connection.cursor()
# Create a table
cursor.execute("CREATE TABLE example (id INTEGER PRIMARY KEY, name TEXT)")
# Insert data into the table
cursor.execute("INSERT INTO example (id, name) VALUES (1, 'John Doe')")
# Commit the changes
connection.commit()
# Query the data
cursor.execute("SELECT * FROM example")
rows = cursor.fetchall()
for row in rows:
    print(row)
# Close the connection
connection.close()


import tweepy
# Connect to the Twitter API
auth = tweepy.OAuthHandler("consumer_key", "consumer_secret")
auth.set_access_token("access_token", "access_token_secret")
api = tweepy.API(auth)
# Search for tweets
tweets = api.search(q="example", count=100)
# Print the text of the tweets
for tweet in tweets:
    print(tweet.text)

