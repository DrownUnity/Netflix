import matplotlib.pyplot as plt
import pandas as pd

netflix_df = pd.read_csv("./netflix_data.csv")

# Changing data type

netflix_df["title"] = netflix_df['genre'].astype('string')
netflix_df["type"] = netflix_df['type'].astype('string')
netflix_df["genre"] = netflix_df['genre'].astype('string')
netflix_df["country"] = netflix_df["country"].astype('string')

print(netflix_df.info())

# Deleting Shows from the DB

netflix_df.drop(netflix_df[netflix_df['type'] == 'TV Show'].index, inplace=True)

# Group by genre

genre_counts = netflix_df['genre'].value_counts()

plt.figure(figsize=(10, 6))
genre_counts.plot(kind='bar', color='skyblue')
plt.title('Movies per Genre')
plt.xlabel('Genre')
plt.ylabel('Amount of Movies')
plt.xticks(range(len(genre_counts.index)), genre_counts.index, rotation=45)
plt.show()

# Average duration

print(netflix_df["duration"].mean())
