
import streamlit as st
import plotly.express as px

def plot_accidents(df):
    fig = px.line(df, x='date', y='accidents', title="Daily Accidents Over Time")
    st.plotly_chart(fig)