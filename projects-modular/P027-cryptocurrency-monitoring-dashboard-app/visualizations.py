
import streamlit as st
import plotly.express as px

def plot_crypto_prices(df):
    fig = px.line(df, x='date', y='close', color='symbol', title="Cryptocurrency Prices")
    st.plotly_chart(fig)