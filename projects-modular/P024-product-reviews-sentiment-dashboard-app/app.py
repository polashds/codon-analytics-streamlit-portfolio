
import streamlit as st
from data_utils import load_data
from analysis import analyze_sentiment
from visualizations import plot_sentiment_distribution

st.title("Product Review Sentiment Dashboard")

file = st.file_uploader("Upload CSV with 'review_text'", type='csv')
if file:
    df = load_data(file)
    st.dataframe(df.head())

    df = analyze_sentiment(df)
    st.dataframe(df[['review_text','sentiment']])
    plot_sentiment_distribution(df)