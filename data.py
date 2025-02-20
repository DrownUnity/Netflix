import matplotlib.pyplot as plt
import pandas as pd

netflix_df = pd.read_csv("./netflix_data.csv")

# Changing data type

netflix_df["title"] = netflix_df['genre'].astype('string')
netflix_df["type"] = netflix_df['type'].astype('string')
netflix_df["genre"] = netflix_df['genre'].astype('string')
netflix_df["country"] = netflix_df["country"].astype('string')

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

avg_duration = netflix_df["duration"].mean()

bins = [0, 30, 60, 90, 120, 150, 180]
labels = ["0-30", "31-60", "61-90", "91-120", "121-150", "151-180"]

netflix_df["duration_bins"] = pd.cut(netflix_df["duration"], bins=bins, labels=labels, right=False)
netflix_df["duration_bins"].value_counts().plot(kind="bar")
plt.xlabel("Duration")
plt.axhline(avg_duration, color="red", linestyle="--", label=f"Avg Duration: {avg_duration:.2f} mins")
plt.xticks(rotation=0)
plt.show()