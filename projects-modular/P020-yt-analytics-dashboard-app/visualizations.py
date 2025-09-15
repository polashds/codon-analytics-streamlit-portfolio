
import streamlit as st
import plotly.express as px

def plot_metrics(df):
    fig = px.scatter(df, x='views', y='engagement_rate', color='video', size='views',
                     title="Video Engagement Rate vs Views")
    st.plotly_chart(fig)