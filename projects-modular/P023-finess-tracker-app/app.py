
import streamlit as st
from data_utils import load_data
from analysis import compute_metrics
from visualizations import plot_metrics

st.title("Fitness Tracker Analysis Dashboard")

file = st.file_uploader("Upload CSV with 'date','steps','calories','distance'", type='csv')
if file:
    df = load_data(file)
    st.dataframe(df.head())

    metrics = st.multiselect("Select Metrics to Visualize", ['steps','calories','distance'], default=['steps'])
    df_metrics = compute_metrics(df, metrics)
    plot_metrics(df_metrics, metrics)