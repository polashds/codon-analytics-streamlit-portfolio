
import streamlit as st
from utils import get_weather
import pandas as pd

st.title("Interactive Weather Forecast Dashboard")

city = st.text_input("Enter City Name")
api_key = st.text_input("Enter OpenWeatherMap API Key")

if st.button("Get Weather") and city and api_key:
    weather_data = get_weather(city, api_key)
    if weather_data:
        df = pd.DataFrame([weather_data])
        st.dataframe(df)
    else:
        st.error("City not found or API error")