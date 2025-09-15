
import streamlit as st
from data_utils import load_data
from analysis import aggregate_consumption
from visualizations import plot_consumption

st.title("Energy Consumption Monitoring Dashboard")

file = st.file_uploader("Upload CSV with 'date','appliance','consumption'", type='csv')
if file:
    df = load_data(file)
    st.dataframe(df.head())

    appliance = st.selectbox("Select Appliance", df['appliance'].unique())
    df_appliance = df[df['appliance']==appliance]

    df_agg = aggregate_consumption(df_appliance)
    plot_consumption(df_agg, appliance)