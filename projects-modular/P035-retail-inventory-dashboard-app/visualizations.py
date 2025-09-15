
import streamlit as st
import plotly.express as px

def plot_inventory_levels(df):
    fig = px.bar(df, x='product', y='stock_level', title="Stock Levels per Product")
    st.plotly_chart(fig)