
import streamlit as st
from data_utils import load_stock_data
from analysis import compute_technical_indicators
from visualizations import plot_stock_with_indicators

st.title("Stock Price & Technical Indicators Dashboard")

file = st.file_uploader("Upload CSV with 'date','symbol','close'", type='csv')
if file:
    df = load_stock_data(file)
    st.dataframe(df.head())

    symbol = st.selectbox("Select Stock", df['symbol'].unique())
    df_stock = df[df['symbol']==symbol]
    df_stock = compute_technical_indicators(df_stock)
    plot_stock_with_indicators(df_stock, symbol)