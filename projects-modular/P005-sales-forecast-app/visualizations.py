
import streamlit as st
import plotly.express as px

def plot_forecast(df, forecast):
    fig = px.line(forecast, x='ds', y='yhat', title="Sales Forecast")
    st.plotly_chart(fig)