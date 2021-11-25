import streamlit as st
import pandas as pd

#iniatlise page and data
st.title("Hello, I am Harshad... ")
st.write( " and I help you to find a movie or a tvshows for tonight")

moviesdata = pd.read_csv('csv/movies.csv')
tvshowdata = pd.read_csv('csv/tvshows.csv')

def choose_movie_or_tvshow ():
    """ Add a sidebar on the left for select movies of tvshows"""
    add_selectbox = st.sidebar.selectbox(
    "Do you want see...?",
    ("A movie", "A Tv show")
    )
    if add_selectbox == "A movie":
        st.write("This is the top 250 of movies by IMDB:")
        st.write(moviesdata)
    else:
        st.write(tvshowdata)

choose_movie_or_tvshow()

st.sidebar.selectbox(
"Have you... a favorite actor or actrice?",
pd.Series
 )



