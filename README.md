# Netflix Dataset - Exploratory Data Analysis (EDA)

## Project Description
This project performs a complete Exploratory Data Analysis on the Netflix Movies and TV Shows dataset to uncover patterns related to content type, genres, countries, ratings, and release trends.

It was developed as part of the **CodeAlpha Data Analytics Internship**.

---

## Objectives
- Understand Netflix's content library
- Identify top genres and producing countries
- Analyze content trends across years
- Generate business-ready insights

---

## Dataset Information
- **Source:** Kaggle - Netflix Movies and TV Shows
- **File:** `netflix_titles.csv`
- **Rows:** ~8800
- **Columns:** 12

### Columns
| Column | Description |
|--------|-------------|
| show_id | Unique identifier |
| type | Movie or TV Show |
| title | Title name |
| director | Director |
| cast | Main cast |
| country | Country of production |
| date_added | Date added to Netflix |
| release_year | Original release year |
| rating | Audience rating |
| duration | Length (minutes or seasons) |
| listed_in | Genre categories |
| description | Short summary |

---

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## Installation
```bash
git clone https://github.com/<your-username>/CodeAlpha_EDA.git
cd CodeAlpha_EDA
pip install -r requirements.txt
```

---

## Usage
Run the script:
```bash
python src/eda_analysis.py
```

Or open the notebook:
```bash
jupyter notebook notebooks/Netflix_EDA.ipynb
```

---

## Visualizations
All generated charts are stored inside the `images/` folder:
- `movies_vs_tvshows.png`
- `content_by_year.png`
- `top_countries.png`
- `genre_distribution.png`
- `duration_analysis.png`
- `ratings_distribution.png`
- `content_added_trend.png`
- `correlation_heatmap.png`

---

## Key Insights
1. Movies make up ~70% of the Netflix catalog.
2. Content additions peaked between 2018–2020.
3. United States, India, and the UK lead content production.
4. TV-MA is the most common rating.
5. Average movie length is around 99 minutes.
6. Most TV Shows have only 1 season.
7. International Movies, Dramas, and Comedies are top genres.
8. Documentaries and kids' content are niche but rising.
9. Netflix adds older catalog content frequently.
10. 2021 saw a drop due to COVID-19 production halts.

---

## Results
The analysis successfully revealed Netflix's library composition, growth patterns, and strategic content focus. 15+ business insights are documented in this repository.

---

## Future Improvements
- Build an interactive Streamlit dashboard
- Create a Power BI / Tableau version
- Add NLP analysis on title descriptions
- Build a recommendation system
- Integrate IMDb ratings
- Add time-series forecasting

---

## Author
**<Your Name>**
Data Analytics Intern @ CodeAlpha
[LinkedIn](https://linkedin.com/in/<your-id>) | [GitHub](https://github.com/<your-username>)
