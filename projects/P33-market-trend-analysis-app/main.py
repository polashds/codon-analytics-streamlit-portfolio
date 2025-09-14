
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Market Trend Analysis App")

file = st.file_uploader("Upload CSV with product & price", type='csv')
if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())

    product = st.selectbox("Select Product", df['product'].unique())
    fig = px.line(df[df['product']==product], x='date', y='price', title=f"Price Trend for {product}")
    st.plotly_chart(fig)