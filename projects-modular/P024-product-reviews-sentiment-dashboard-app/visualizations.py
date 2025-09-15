
import streamlit as st
import plotly.express as px

def plot_sentiment_distribution(df):
    fig = px.histogram(df, x='sentiment', title="Sentiment Distribution of Product Reviews")
    st.plotly_chart(fig)