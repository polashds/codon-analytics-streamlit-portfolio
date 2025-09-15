
import streamlit as st
from data_utils import load_data
from model_utils import recommend_movies

st.title("Movie Recommendation Dashboard")

file = st.file_uploader("Upload CSV with 'movie','genre','rating'", type='csv')
if file:
    df = load_data(file)
    st.dataframe(df.head())

    selected_movie = st.selectbox("Select a Movie", df['movie'].unique())
    recommendations = recommend_movies(df, selected_movie)
    st.subheader(f"Movies similar to {selected_movie}:")
    st.write(recommendations)