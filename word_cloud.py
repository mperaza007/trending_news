from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import sqlite3

# Get text from news data articles titles
connection = sqlite3.connect("news_data.db")
cursor = connection.cursor()
cursor.execute("SELECT title FROM news")
rows = cursor.fetchall()
connection.close()

# Get the text from the rows
text = " ".join([row[0] for row in rows])

custom_stopwords = set(STOPWORDS) #STOPWORDS is a set of common words to exclude that comes with the wordcloud library
custom_stopwords.update([ "Korea", "Times", "S", "U"]) 

# Create and display word cloud
wordcloud = WordCloud(width=800, height=400, max_words=100, background_color='white', stopwords=custom_stopwords).generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()