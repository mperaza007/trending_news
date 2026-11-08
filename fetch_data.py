import requests
import sqlite3
from datetime import datetime
from dotenv import load_dotenv
import os

#current time
current_time = datetime.now()

# Load variables from .env file
load_dotenv()

# Retrieve the API key
api_key = os.getenv("API_KEY")

# fetch data from currents api
base_url = "https://api.currentsapi.services/v1/latest-news"
headers = {"Authorization": api_key}
params = {
    "language": "en",
    "region": "us",
}
request = requests.get(base_url, headers= headers, params = params)

request_data = request.json()

#connect to sqlte3 database
connection = sqlite3.connect("news_data.db")
cursor = connection.cursor()

#create table for news data
command = """
CREATE TABLE IF NOT EXISTS news(
id TEXT PRIMARY KEY, title TEXT, description TEXT, categories TEXT, author TEXT, time_published TEXT, time_fetched TEXT)
"""
cursor.execute(command)

#insert data into the table, commit and close the connection
for article in request_data['news']:
    if article['id'] and article['title'] and article['published'] and article['category'] and article ['author']:
        cursor.execute("INSERT OR IGNORE INTO news VALUES(?,?,?,?,?,?,?)", (article['id'], article['title'], article['description'], 
                                                                        ",".join(article['category']), article['author'], article['published'], current_time))
connection.commit()

connection.close()



