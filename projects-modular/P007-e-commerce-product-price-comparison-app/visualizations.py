
import streamlit as st
import plotly.express as px

def plot_price_comparison(df, product):
    fig = px.bar(df, x='store', y='price', color='store', title=f"Price Comparison for {product}")
    st.plotly_chart(fig)