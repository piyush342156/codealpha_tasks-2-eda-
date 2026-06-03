# =====================================================
# Netflix Movies and TV Shows - Exploratory Data Analysis
# CodeAlpha Data Analytics Internship
# Author: <Your Name>
# =====================================================

# -------- 1. Import Libraries --------
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# Visualization styling
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)
plt.rcParams["axes.titlesize"] = 14
plt.rcParams["axes.labelsize"] = 12

# Folder for saving plots
IMG_DIR = "images"
os.makedirs(IMG_DIR, exist_ok=True)


# -------- 2. Load Dataset --------
df = pd.read_csv("data/netflix_titles.csv")
print("Dataset loaded successfully.")
print("Shape:", df.shape)


# -------- 3. Dataset Inspection --------
print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe(include="all"))


# -------- 4. Missing Value Analysis --------
missing = df.isnull().sum().sort_values(ascending=False)
missing_pct = (missing / len(df)) * 100
missing_df = pd.DataFrame({"Missing Count": missing, "Missing %": missing_pct.round(2)})
print("\nMissing Values:\n", missing_df)


# -------- 5. Duplicate Checking --------
print("\nDuplicate rows:", df.duplicated().sum())


# -------- 6. Data Cleaning --------
# Fill missing categorical values
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna(df["rating"].mode()[0])

# Drop rows where date_added or duration is missing (very few rows)
df = df.dropna(subset=["date_added", "duration"])

# Remove duplicates if any
df = df.drop_duplicates()


# -------- 7. Data Type Conversion --------
df["date_added"] = pd.to_datetime(df["date_added"].str.strip(), errors="coerce")
df["year_added"] = df["date_added"].dt.year
df["month_added"] = df["date_added"].dt.month


# -------- 8. Feature Engineering --------
# Split duration into number + unit
df["duration_int"] = df["duration"].str.extract(r"(\d+)").astype(float)
df["duration_unit"] = df["duration"].str.extract(r"([a-zA-Z]+)")

# Take only the first country (primary producer)
df["main_country"] = df["country"].apply(lambda x: x.split(",")[0].strip())

# Take only the first genre (primary genre)
df["main_genre"] = df["listed_in"].apply(lambda x: x.split(",")[0].strip())


# -------- 9. Analysis A: Movies vs TV Shows --------
type_counts = df["type"].value_counts()
print("\nContent Type Distribution:\n", type_counts)

plt.figure()
sns.countplot(data=df, x="type", palette="Set2")
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Content Type")
plt.ylabel("Count")
plt.savefig(f"{IMG_DIR}/movies_vs_tvshows.png", bbox_inches="tight")
plt.close()


# -------- 10. Analysis B: Content Released by Year --------
plt.figure()
year_trend = df["release_year"].value_counts().sort_index()
year_trend = year_trend[year_trend.index >= 1990]
year_trend.plot(kind="line", marker="o", color="crimson")
plt.title("Number of Titles Released Each Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.savefig(f"{IMG_DIR}/content_by_year.png", bbox_inches="tight")
plt.close()


# -------- 11. Analysis C: Top 10 Countries --------
top_countries = df[df["main_country"] != "Unknown"]["main_country"].value_counts().head(10)
print("\nTop 10 Countries:\n", top_countries)

plt.figure()
sns.barplot(x=top_countries.values, y=top_countries.index, palette="viridis")
plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.savefig(f"{IMG_DIR}/top_countries.png", bbox_inches="tight")
plt.close()


# -------- 12. Analysis D: Top Genres --------
top_genres = df["main_genre"].value_counts().head(10)
print("\nTop 10 Genres:\n", top_genres)

plt.figure()
sns.barplot(x=top_genres.values, y=top_genres.index, palette="magma")
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")
plt.savefig(f"{IMG_DIR}/genre_distribution.png", bbox_inches="tight")
plt.close()


# -------- 13. Analysis E: Duration Analysis --------
movies = df[df["type"] == "Movie"]
tv_shows = df[df["type"] == "TV Show"]

print("\nMovie average duration (min):", movies["duration_int"].mean().round(2))
print("TV Show average seasons:", tv_shows["duration_int"].mean().round(2))

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
sns.histplot(movies["duration_int"], bins=30, kde=True, ax=axes[0], color="steelblue")
axes[0].set_title("Movie Duration Distribution (Minutes)")
axes[0].set_xlabel("Minutes")

sns.countplot(x=tv_shows["duration_int"], ax=axes[1], palette="coolwarm")
axes[1].set_title("TV Show Seasons Distribution")
axes[1].set_xlabel("Number of Seasons")

plt.tight_layout()
plt.savefig(f"{IMG_DIR}/duration_analysis.png", bbox_inches="tight")
plt.close()


# -------- 14. Analysis F: Ratings --------
plt.figure()
rating_counts = df["rating"].value_counts().head(10)
sns.barplot(x=rating_counts.index, y=rating_counts.values, palette="cubehelix")
plt.title("Most Common Ratings on Netflix")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.savefig(f"{IMG_DIR}/ratings_distribution.png", bbox_inches="tight")
plt.close()


# -------- 15. Analysis G: Content Added Over Time --------
plt.figure()
added_trend = df["year_added"].value_counts().sort_index()
added_trend.plot(kind="bar", color="teal")
plt.title("Titles Added to Netflix Per Year")
plt.xlabel("Year Added")
plt.ylabel("Count")
plt.savefig(f"{IMG_DIR}/content_added_trend.png", bbox_inches="tight")
plt.close()


# -------- 16. Analysis H: Correlation Heatmap --------
plt.figure()
corr = df[["release_year", "year_added", "month_added", "duration_int"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap of Numeric Features")
plt.savefig(f"{IMG_DIR}/correlation_heatmap.png", bbox_inches="tight")
plt.close()


print("\nEDA completed. All charts saved in 'images/' folder.")
