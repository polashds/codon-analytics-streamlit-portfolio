
import streamlit as st
import pandas as pd
from prophet import Prophet
import plotly.express as px

st.title("E-commerce Sales Forecasting")

file = st.file_uploader("Upload CSV with 'date' & 'sales'", type='csv')
if file:
    df = pd.read_csv(file)
    df = df.rename(columns={'date':'ds','sales':'y'})
    st.dataframe(df.head())

    if st.button("Forecast Sales"):
        model = Prophet()
        model.fit(df)
        future = model.make_future_dataframe(periods=30)
        forecast = model.predict(future)
        fig = px.line(forecast, x='ds', y='yhat', title="Sales Forecast")
        st.plotly_chart(fig)
        forecast.to_csv("sales_forecast.csv", index=False)
        st.success("Forecast complete & saved")
