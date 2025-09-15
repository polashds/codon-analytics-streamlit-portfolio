
import streamlit as st
import plotly.express as px

def plot_stock_comparison(df, symbols):
    filtered_df = df[df['symbol'].isin(symbols)]
    fig = px.line(filtered_df, x='date', y='close', color='symbol', title="Stock Price Comparison")
    st.plotly_chart(fig)