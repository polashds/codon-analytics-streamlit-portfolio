
import streamlit as st
from data_utils import load_data
from visualizations import plot_energy_trend

st.title("Energy Consumption Dashboard")

file = st.file_uploader("Upload CSV with 'date','consumption'", type='csv')
if file:
    df = load_data(file)
    st.dataframe(df.head())
    plot_energy_trend(df)