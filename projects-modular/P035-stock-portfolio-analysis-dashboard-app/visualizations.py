
import streamlit as st
import plotly.express as px

def plot_portfolio_performance(df):
    fig = px.line(df, x='date', y='portfolio_value', color='symbol', title="Portfolio Value Over Time")
    st.plotly_chart(fig)