
import streamlit as st
import plotly.express as px

def plot_aqi_trend(df):
    fig = px.line(df, x='date', y='AQI', title="Air Quality Index Over Time")
    st.plotly_chart(fig)