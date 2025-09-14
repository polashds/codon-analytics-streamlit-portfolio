
import streamlit as st
import pandas as pd

st.title("Product Price Comparison")

file = st.file_uploader("Upload CSV of product prices", type='csv')
if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())

    product = st.selectbox("Select Product", df['product_name'].unique())
    st.subheader(f"Price Comparison for {product}")
    st.bar_chart(df[df['product_name']==product]['price'])