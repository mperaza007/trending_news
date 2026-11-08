import sqlite3
from collections import Counter
import matplotlib.pyplot as plt

# connect to the database
connection = sqlite3.connect("news_data.db")
cursor = connection.cursor()

# pull the categories column
cursor.execute("SELECT categories FROM news")
rows = cursor.fetchall()
connection.close()

# split each comma-separated string and count every category
counter = Counter()
for (categories,) in rows:
        for category in categories.split(","):
            #exclude regional and general categories
            if category.strip().lower() in {"regional", "general"}:
                    continue
            counter[category.strip().lower()] += 1

# get the top 10 categories
top_categories = counter.most_common(10)
labels = [category for category, count in top_categories]
counts = [count for category, count in top_categories]

colors = ["blue","green","red","yellow","purple","orange", "brown", "pink", "gray", "cyan"]

# plot the bar chart
plt.figure(figsize=(10, 6))
plt.bar(labels, counts, color=colors)
plt.title("Top News Categories")
plt.xlabel("Category")
plt.ylabel("Number of Articles")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()