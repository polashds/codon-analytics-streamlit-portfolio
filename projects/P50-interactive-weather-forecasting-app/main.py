
import streamlit as st
import requests
import pandas as pd

st.title("Weather Forecast App")

city = st.text_input("Enter City Name")
api_key = "YOUR_OPENWEATHERMAP_API_KEY"

if st.button("Get Weather"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    res = requests.get(url).json()
    if res.get('main'):
        st.write(f"Temperature: {res['main']['temp']} °C")
        st.write(f"Humidity: {res['main']['humidity']}%")
        st.write(f"Weather: {res['weather'][0]['description']}")
    else:
        st.error("City not found")