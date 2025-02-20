import matplotlib.pyplot as plt
import pandas as pd

netflix_df = pd.read_csv("./netflix_data.csv")

# Changing data type

netflix_df["title"] = netflix_df['genre'].astype('string')
netflix_df["type"] = netflix_df['type'].astype('category')
netflix_df["genre"] = netflix_df['genre'].astype('category')
netflix_df["country"] = netflix_df["country"].astype('string')

# Data exploration

unique_genres = set(netflix_df['genre'])

genres = []

for genre in unique_genres:
    genres.append(genre)

print(genres)