
import streamlit as st
from data_utils import load_data
from analysis import compute_portfolio_returns
from visualizations import plot_portfolio_performance

st.title("Stock Portfolio Analysis Dashboard")

file = st.file_uploader("Upload CSV with 'date','symbol','closing_price','shares'", type='csv')
if file:
    df = load_data(file)
    st.dataframe(df.head())

    portfolio = st.multiselect("Select Stock Symbols", df['symbol'].unique(), default=df['symbol'].unique()[:3])
    df_selected = df[df['symbol'].isin(portfolio)]

    df_selected = compute_portfolio_returns(df_selected)
    st.dataframe(df_selected.head())

    plot_portfolio_performance(df_selected)