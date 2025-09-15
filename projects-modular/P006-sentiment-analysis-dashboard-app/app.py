
import streamlit as st
from data_utils import load_data
from analysis import analyze_sentiment
from visualizations import plot_sentiment_distribution

st.title("Interactive Sentiment Analysis Dashboard")

file = st.file_uploader("Upload CSV with 'text' column", type='csv')
if file:
    df = load_data(file)
    st.dataframe(df.head())

    if st.button("Analyze Sentiment"):
        df = analyze_sentiment(df)
        st.dataframe(df.head())
        plot_sentiment_distribution(df)