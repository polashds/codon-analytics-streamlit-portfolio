
import streamlit as st
from data_utils import load_data
from model_utils import train_forecast_model, make_forecast
from visualizations import plot_forecast

st.title("Sales Forecasting Dashboard")

file = st.file_uploader("Upload CSV with 'date' & 'sales'", type='csv')
if file:
    df = load_data(file)
    st.dataframe(df.head())

    periods = st.number_input("Forecast Period (days)", min_value=1, max_value=365, value=30)
    if st.button("Forecast Sales"):
        model = train_forecast_model(df)
        forecast = make_forecast(model, periods)
        plot_forecast(df, forecast)
        st.success("Sales forecast completed")