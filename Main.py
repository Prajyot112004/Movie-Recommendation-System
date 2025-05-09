import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=f7f2faaba0ad50095df7ea0802b878a7".format(movie_id)
    data = requests.get(url)
    data=data.json()
    poster_path=data['poster_path']
    full_path="https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(option):
    movie_index=movies[movies["title"]==option].index[0]
    distances=similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommend_movies=[]
    recommend_movie_poster=[]

    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id

        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_movie_poster.append(fetch_poster(movie_id))

    return recommend_movies, recommend_movie_poster

if __name__=="__main__":

    similarity = pickle.load(open("similarity.pkl","rb"))
    movies = pickle.load(open("movies.pkl","rb"))

    st.title("Movie Recommendation System")

    option=st.selectbox("Enter Movie You want to select:" , movies['title'].values)

    if st.button("Recommend"):
        recommended_names, recommended_poster=recommend(option)
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.text(recommended_names[0])
            st.image(recommended_poster[0])
        with col2:
            st.text(recommended_names[1])
            st.image(recommended_poster[1])
        with col3:
            st.text(recommended_names[2])
            st.image(recommended_poster[2])
        with col4:
            st.text(recommended_names[3])
            st.image(recommended_poster[3])
        with col5:
            st.text(recommended_names[4])
            st.image(recommended_poster[4])
