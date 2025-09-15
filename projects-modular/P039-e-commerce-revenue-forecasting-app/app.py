
import streamlit as st
from data_utils import load_data
from model_utils import forecast_revenue
from visualizations import plot_revenue_forecast

st.title("E-commerce Revenue Forecasting Dashboard")

file = st.file_uploader("Upload CSV with 'date','revenue'", type='csv')
if file:
    df = load_data(file)
    st.dataframe(df.head())

    forecast_df = forecast_revenue(df)
    st.dataframe(forecast_df)

    plot_revenue_forecast(df, forecast_df)