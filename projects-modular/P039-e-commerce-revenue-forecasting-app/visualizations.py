
import streamlit as st
import plotly.express as px

def plot_revenue_forecast(df, forecast_df):
    fig = px.line(df, x='date', y='revenue', title="Revenue Forecast")
    fig.add_scatter(x=forecast_df['date'], y=forecast_df['forecast'], mode='lines', name='Forecast')
    st.plotly_chart(fig)