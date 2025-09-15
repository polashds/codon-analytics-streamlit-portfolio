
import streamlit as st
from data_utils import load_data
from analysis import get_product_prices
from visualizations import plot_price_comparison

st.title("E-commerce Product Price Comparison Dashboard")

file = st.file_uploader("Upload CSV with 'product','store','price'", type='csv')
if file:
    df = load_data(file)
    st.dataframe(df.head())

    product = st.selectbox("Select Product", df['product'].unique())
    price_data = get_product_prices(df, product)
    plot_price_comparison(price_data, product)