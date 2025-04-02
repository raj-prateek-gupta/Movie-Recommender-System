import streamlit as st
import pandas as pd
import pickle
import requests
import joblib

# Load movies list DataFrame
movies_df = pickle.load(open('model/movies_list.pkl', 'rb'))

# Extract movie titles as a list
movies_list = movies_df['title'].tolist()

# Load similarity matrix
similarity = joblib.load('model/similarity.pkl')

# Recommender Function
def recommend(movie):
    if movie not in movies_list:
        return ["Movie not found!"]

    # Get index of the selected movie
    index = movies_df[movies_df['title'] == movie].index[0]

    # Get similarity scores
    distances = similarity[index]

    # Get top 5 most similar movies
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies_df.iloc[i[0]]['title'])  # Fixing indexing issue

    return recommended_movies

# Title 
st.title("Movie Recommender System")

# Dropdown for movie selection
select_movie = st.selectbox('Your favorite movie', movies_list)

# Button to generate recommendations
if st.button('Recommend'):
    recommendations = recommend(select_movie)
    for movie in recommendations:
        st.write(movie)
