import streamlit as st
import pickle
import random

# ---------------- Page config ----------------
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
    <style>
    .main-title {
        font-size: 3rem; font-weight: 800; text-align: center;
        background: linear-gradient(90deg, #ff6b6b, #feca57);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .subtitle {
        text-align: center; color: #888; margin-bottom: 30px;
    }
    .poster {
        border-radius: 12px;
        padding: 30px 12px;
        text-align: center;
        color: white;
        font-weight: 700;
        font-size: 1rem;
        height: 220px;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    .stButton>button {
        background: linear-gradient(90deg, #ff6b6b, #feca57);
        color: white; border: none; border-radius: 8px;
        padding: 10px 24px; font-weight: 600; width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- Load model ----------------
@st.cache_resource
def load_data():
    movies = pickle.load(open('movies.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    return movies, similarity

movies, similarity = load_data()

EMOJIS = ["🎬", "🍿", "🎥", "🌟", "🔥", "🎭", "🚀", "💥", "🌈", "🎯"]

# ---------------- Recommend ----------------
def recommend(movie):
    idx = movies[movies['title'] == movie].index[0]
    distances = similarity[idx]
    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]
    return [movies.iloc[i[0]].title for i in movie_list]

# ---------------- UI ----------------
st.markdown('<h1 class="main-title">🎬 Movie Recommender</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Content-based recommendations using cosine similarity</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    selected_movie = st.selectbox(
        "Choose a movie",
        movies['title'].values,
        index=None,
        placeholder="Type or select a movie..."
    )
    recommend_btn = st.button("🔍 Recommend", use_container_width=True)

if recommend_btn and selected_movie:
    with st.spinner("Finding similar movies..."):
        recs = recommend(selected_movie)

    st.markdown("### 🍿 You might also like:")
    cols = st.columns(5)
    for col, name, emoji in zip(cols, recs, random.sample(EMOJIS, 5)):
        c1 = random.choice(["#ff6b6b", "#feca57", "#48dbfb", "#1dd1a1", "#5f27cd"])
        c2 = random.choice(["#ee5253", "#ff9f43", "#0abde3", "#10ac84", "#341f97"])
        with col:
            st.markdown(
                f'<div class="poster" style="background: linear-gradient(135deg, {c1}, {c2});">'
                f'{emoji}<br><br>{name}</div>',
                unsafe_allow_html=True
            )

# ---------------- Footer ----------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:#666; font-size:0.85rem;'>"
    "Built with ❤️ using Streamlit · scikit-learn"
    "</p>",
    unsafe_allow_html=True
)