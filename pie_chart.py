import sqlite3
from collections import Counter
import matplotlib.pyplot as plt

def get_category_counts():
    connection = sqlite3.connect("news_data.db")
    cursor = connection.cursor()
    cursor.execute("SELECT categories FROM news")
    rows = cursor.fetchall()
    connection.close()

    counter = Counter()
    for (categories,) in rows:
        if categories:
            for category in categories.split(","):
               #exclude regional and general categories
               if category.strip().lower() in {"regional", "general"}:
                    continue
               counter[category.strip().lower()] += 1
    return counter

counter = get_category_counts()
top = counter.most_common(10)

labels = [c for c, n in top]
counts = [n for c, n in top]

plt.figure(figsize=(8, 8))
plt.pie(counts, labels=labels, autopct="%1.1f%%", startangle=90)
plt.title("Share of News Categories")
plt.show()