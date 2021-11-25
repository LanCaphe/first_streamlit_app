import streamlit as st
import pandas as pd

#structure page
st.title("Mon moteur de recherche de films et séries")

data = pd.read_csv('movies.csv')
 

st.write(data)