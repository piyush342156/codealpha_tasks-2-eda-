# Netflix Dataset - EDA Project Report
**CodeAlpha Data Analytics Internship**

---

## Abstract
This project performs a comprehensive Exploratory Data Analysis (EDA) on the Netflix Movies and TV Shows dataset using Python. The objective is to understand the structure, distribution, and trends in Netflix's content catalog. Key findings include the dominance of movies over TV shows, the leading role of the US, India, and UK in content production, and a sharp rise in content additions after 2016. The analysis produced 8+ visualizations and 15+ business insights useful for content-strategy decisions.

---

## 1. Introduction
Netflix is one of the world's largest streaming platforms. Understanding what content dominates the platform helps content teams make better licensing, production, and audience-targeting decisions. This project uses EDA to explore the Netflix dataset and translate the findings into business insights.

---

## 2. Dataset Description
- **Source:** Kaggle - Netflix Movies and TV Shows
- **Rows:** ~8800
- **Columns:** 12
- **File:** netflix_titles.csv

Columns include: show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description.

---

## 3. Methodology
- Loaded dataset using Pandas
- Inspected schema, types, and missing values
- Cleaned and transformed data
- Engineered new features (year_added, main_country, main_genre, duration_int)
- Visualized findings using Matplotlib and Seaborn
- Documented business insights

---

## 4. Data Cleaning
| Step | Action | Reason |
|------|--------|--------|
| 1 | Filled director/cast/country with "Unknown" | High missing % |
| 2 | Filled rating with mode | Categorical |
| 3 | Dropped rows missing date_added/duration | Very few rows |
| 4 | Removed duplicates | Data integrity |
| 5 | Converted date_added to datetime | Time analysis |
| 6 | Split duration into number + unit | Mixed units |
| 7 | Extracted main country & genre | Multi-value columns |

---

## 5. Analysis

### A. Movies vs TV Shows
Movies dominate (~70%) over TV Shows (~30%).

### B. Content Released by Year
Sharp increase after 2015; peak in 2018–2020; dip in 2021.

### C. Top 10 Countries
United States, India, and the UK lead. Top 10 contribute over 80% of titles.

### D. Genres
International Movies, Dramas, and Comedies dominate. Documentaries growing.

### E. Duration
Avg movie length ~99 min. Most TV Shows have 1 season.

### F. Ratings
TV-MA leads, followed by TV-14 and TV-PG.

### G. Content Added Over Time
Peak addition years are 2019 and 2020.

### H. Correlation
Weak correlation between release_year and year_added (~0.3).

---

## 6. Visualizations
- movies_vs_tvshows.png
- content_by_year.png
- top_countries.png
- genre_distribution.png
- duration_analysis.png
- ratings_distribution.png
- content_added_trend.png
- correlation_heatmap.png

---

## 7. Findings (Business Insights)
1. Movies dominate the Netflix catalog.
2. Content additions peaked 2018–2020.
3. US, India, and UK lead production.
4. TV-MA dominates ratings.
5. Avg movie length is ~99 min.
6. Most TV Shows have 1 season.
7. 2021 dip due to COVID-19.
8. International content is rising.
9. Netflix adds older catalog content frequently.
10. Kids' content is underrepresented.
11. Documentaries are a growing niche.
12. Adult audiences are Netflix's primary target.
13. Drama is the most consistent genre.
14. Regional originals are gaining importance (India, Korea, Spain).
15. Top 10 countries contribute over 80% of content.

---

## 8. Conclusion
Netflix's catalog leans heavily toward movies and adult audiences, with strong regional contributions from US, India, and UK. Content additions skyrocketed after 2016. Future strategy should focus on expanding TV Shows, kids' content, and underrepresented regions.

---

## 9. References
- Kaggle Dataset: https://www.kaggle.com/datasets/shivamb/netflix-shows
- Pandas Documentation: https://pandas.pydata.org/
- Seaborn Documentation: https://seaborn.pydata.org/
- Matplotlib Documentation: https://matplotlib.org/
