
import streamlit as st
from data_utils import load_data
from analysis import compute_occupancy_stats
from visualizations import plot_occupancy_trend

st.title("Hospital Bed Occupancy Dashboard")

file = st.file_uploader("Upload CSV with 'date','department','occupied_beds','total_beds'", type='csv')
if file:
    df = load_data(file)
    st.dataframe(df.head())

    department = st.selectbox("Select Department", df['department'].unique())
    df_dept = df[df['department']==department]

    stats = compute_occupancy_stats(df_dept)
    st.write(stats)

    plot_occupancy_trend(df_dept)