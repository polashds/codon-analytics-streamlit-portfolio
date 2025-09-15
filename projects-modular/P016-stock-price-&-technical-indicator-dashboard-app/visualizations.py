
import streamlit as st
import plotly.graph_objects as go

def plot_stock_with_indicators(df, symbol):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['date'], y=df['close'], name='Close Price'))
    fig.add_trace(go.Scatter(x=df['date'], y=df['SMA_20'], name='SMA 20'))
    fig.add_trace(go.Scatter(x=df['date'], y=df['SMA_50'], name='SMA 50'))
    fig.update_layout(title=f"{symbol} Price & Technical Indicators", xaxis_title="Date", yaxis_title="Price")
    st.plotly_chart(fig)