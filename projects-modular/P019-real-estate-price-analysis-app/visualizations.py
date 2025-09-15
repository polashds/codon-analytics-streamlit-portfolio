
import streamlit as st
import plotly.express as px

def plot_price_distribution(df):
    fig = px.histogram(df, x='price', nbins=30, title="Price Distribution")
    st.plotly_chart(fig)