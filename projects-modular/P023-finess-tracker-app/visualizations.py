
import streamlit as st
import plotly.express as px

def plot_metrics(df, metrics):
    for metric in metrics:
        fig = px.line(df, x='date', y=metric, title=f"{metric.title()} Over Time")
        st.plotly_chart(fig)