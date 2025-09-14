
import streamlit as st
import pandas as pd
from textblob import TextBlob

st.title("Social Media Sentiment Analysis")

file = st.file_uploader("Upload CSV with posts", type='csv')
if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())

    if st.button("Analyze Sentiment"):
        df['polarity'] = df['text'].apply(lambda x: TextBlob(x).sentiment.polarity)
        df['sentiment'] = df['polarity'].apply(lambda x: 'Positive' if x>0 else ('Negative' if x<0 else 'Neutral'))
        st.dataframe(df.head())
        df.to_csv("sentiment_analysis.csv", index=False)
        st.success("Sentiment analysis complete, saved as sentiment_analysis.csv")