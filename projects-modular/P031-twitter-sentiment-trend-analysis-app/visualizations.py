
import streamlit as st
import plotly.express as px

def plot_sentiment_trend(df):
    trend = df.groupby('date')['polarity'].mean().reset_index()
    fig = px.line(trend, x='date', y='polarity', title="Average Sentiment Over Time")
    st.plotly_chart(fig)