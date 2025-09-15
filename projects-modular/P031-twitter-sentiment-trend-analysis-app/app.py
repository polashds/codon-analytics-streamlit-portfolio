
import streamlit as st
from data_utils import load_data
from analysis import analyze_sentiment
from visualizations import plot_sentiment_trend

st.title("Twitter Sentiment Trend Dashboard")

file = st.file_uploader("Upload CSV with 'tweet_text','date'", type='csv')
if file:
    df = load_data(file)
    st.dataframe(df.head())

    df = analyze_sentiment(df)
    st.dataframe(df[['tweet_text','sentiment']])
    plot_sentiment_trend(df)