
import streamlit as st
from data_utils import load_crypto_data
from analysis import compute_returns
from visualizations import plot_crypto_prices

st.title("Cryptocurrency Dashboard")

file = st.file_uploader("Upload CSV with 'date','symbol','close'", type='csv')
if file:
    df = load_crypto_data(file)
    st.dataframe(df.head())

    symbols = st.multiselect("Select Cryptocurrencies", df['symbol'].unique(), default=df['symbol'].unique()[:2])
    df_selected = df[df['symbol'].isin(symbols)]
    df_selected = compute_returns(df_selected)

    plot_crypto_prices(df_selected)