import streamlit as st
import pandas as pd

#structure page
st.title("Mon moteur de recherche de films et séries")

datamovies = pd.read_csv('csv/movies.csv')

 

st.write(data)