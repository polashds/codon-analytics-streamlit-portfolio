
import streamlit as st
from data_utils import load_data
from analysis import compute_performance_metrics
from visualizations import plot_performance

st.title("Employee Performance Dashboard")

file = st.file_uploader("Upload CSV with 'employee','tasks_completed','hours_worked','rating'", type='csv')
if file:
    df = load_data(file)
    st.dataframe(df.head())

    df_metrics = compute_performance_metrics(df)
    st.dataframe(df_metrics)

    plot_performance(df_metrics)