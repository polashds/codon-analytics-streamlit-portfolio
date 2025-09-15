
import streamlit as st
from data_utils import load_data
from analysis import compute_aqi
from visualizations import plot_aqi_trend

st.title("Air Quality Monitoring Dashboard")

file = st.file_uploader("Upload CSV with 'date','location','pm2.5','pm10'", type='csv')
if file:
    df = load_data(file)
    st.dataframe(df.head())

    location = st.selectbox("Select Location", df['location'].unique())
    df_location = df[df['location']==location]

    df_location = compute_aqi(df_location)
    st.dataframe(df_location[['date','AQI']])

    plot_aqi_trend(df_location)