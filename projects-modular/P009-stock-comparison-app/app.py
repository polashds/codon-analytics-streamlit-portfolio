
import streamlit as st
from data_utils import load_stock_data
from visualizations import plot_stock_comparison

st.title("Interactive Stock Comparison Dashboard")

file = st.file_uploader("Upload CSV with 'date','symbol','close'", type='csv')
if file:
    df = load_stock_data(file)
    st.dataframe(df.head())

    symbols = st.multiselect("Select Stocks to Compare", df['symbol'].unique(), default=df['symbol'].unique()[:2])
    plot_stock_comparison(df, symbols)