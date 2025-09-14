
import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px

st.title("Cryptocurrency Price Tracker")

crypto = st.selectbox("Select Crypto", ["BTC-USD","ETH-USD","BNB-USD"])
start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")

if st.button("Fetch & Plot"):
    df = yf.download(crypto, start=start_date, end=end_date)
    df.reset_index(inplace=True)
    fig = px.line(df, x='Date', y='Close', title=f"{crypto} Closing Price")
    st.plotly_chart(fig)