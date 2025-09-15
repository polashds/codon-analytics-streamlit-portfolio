
import streamlit as st
from data_utils import load_data
from analysis import compute_accident_stats
from visualizations import plot_accidents

st.title("Traffic Accident Analysis Dashboard")

file = st.file_uploader("Upload CSV with 'date','location','accidents','fatalities'", type='csv')
if file:
    df = load_data(file)
    st.dataframe(df.head())

    location = st.selectbox("Select Location", df['location'].unique())
    df_location = df[df['location']==location]

    stats = compute_accident_stats(df_location)
    st.write(stats)

    plot_accidents(df_location)