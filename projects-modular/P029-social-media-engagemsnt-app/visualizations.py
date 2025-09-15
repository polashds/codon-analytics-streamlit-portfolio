
import streamlit as st
import plotly.express as px

def plot_engagement(df):
    fig = px.bar(df, x='post', y='engagement_rate', title="Engagement Rate per Post")
    st.plotly_chart(fig)