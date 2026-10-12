# 🎬 Movie Recommender System

A content-based movie recommendation engine that suggests similar movies using cosine similarity.

![Movie Recommender Screenshot](screenshot.png)

## ✨ Features

- Select any movie from a dropdown
- Get top 5 similar recommendations instantly
- Clean, modern UI with gradient poster cards
- Cached model loading for fast performance

## 🛠️ Tech Stack

- **Python**
- **Streamlit** — interactive web UI
- **scikit-learn** — CountVectorizer + cosine similarity
- **pandas** & **NumPy** — data handling

## ⚙️ How It Works

1. Movie metadata (genres, cast, crew, keywords, overview) is merged into a single "tags" column
2. Text is preprocessed — lowercasing, stemming, whitespace removal
3. Tags are vectorized using **CountVectorizer**
4. **Cosine similarity** is calculated between all movie vectors
5. Top 5 most similar movies are returned for any selected movie

## 🚀 Run Locally

```bash
# Clone the repo
git clone https://github.com/bilal-157/movie-recommender.git
cd movie-recommender

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
