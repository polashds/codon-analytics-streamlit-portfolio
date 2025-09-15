
import streamlit as st
import plotly.express as px

def plot_sales(df):
    fig = px.line(df, x='date', y='sales', title="Daily Sales Over Time")
    st.plotly_chart(fig)