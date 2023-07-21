import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse= True, key = lambda x:x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies['title'][i[0]])
    return recommended_movies

movie_dict = pickle.load(open('movie_dict.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movies = pd.DataFrame(movie_dict)
st.title("Movie Recommender System")

selected_movie_name = st.selectbox('Search for the movie type to recommend',movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
else:
    st.write('Select movie and Press Recommend')