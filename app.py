import streamlit as st
import pickle
import pandas as pd

# Function to recommend movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# Load data and models
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit app title and selection box
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
   "Select a movie to get recommendations:",
   movies['title'].values)

# Recommendation button
if st.button('Recommend'):
    st.subheader("Top 5 Recommended Movies:")
    recommendations = recommend(selected_movie_name)
    for i, movie in enumerate(recommendations, start=1):
        st.write(f"{i}. {movie}")

# Add background image and 3D animation
st.markdown(
"""
<style>
body {
    background-image: url('background_image.jpg');
    background-size: cover;
    background-position: center;
    color: #333;
    font-family: Arial, sans-serif;
    height: 100vh;
    overflow: hidden;
}
.stButton>button {
    background-color: #008CBA;
    color: white;
    padding: 0.5em 1em;
    font-size: 1em;
    border-radius: 0.5em;
    border: none;
}
.stButton>button:hover {
    background-color: #005f79;
}
.stSelectbox>div>div {
    background-color: #ddd;
    border-radius: 0.3em;
}
.stSelectbox>div>div:hover {
    background-color: #ccc;
}
.stSelectbox>div>div>div {
    color: #333;
}
.stMarkdown {
    color: #555;
    font-size: 1.1em;
}
</style>
""",
unsafe_allow_html=True)
