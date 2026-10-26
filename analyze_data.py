import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect and load data from news database
connection = sqlite3.connect("news_data.db")

df = pd.read_sql_query("SELECT date(time_fetched) AS Fetched_Date, categories FROM news", connection)

#Count the number of articles per category per day
category_counts = df.groupby(['Fetched_Date', 'categories']).size().reset_index(name = 'Count')

#Create a line chart for each category
plt.figure(figsize=(12, 6))
for category in category_counts['categories'].unique():
    category_data = category_counts[category_counts['categories'] == category]
    plt.plot(category_data['Fetched_Date'], category_data['Count'], marker = 'o', label = category)
plt.xlabel('Date')
plt.ylabel('Number of Articles')
plt.title('News Articles by Category Over Time')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
