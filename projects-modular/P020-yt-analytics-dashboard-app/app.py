
import streamlit as st
from data_utils import load_data
from analysis import compute_metrics
from visualizations import plot_metrics

st.title("YouTube Video Analytics Dashboard")

file = st.file_uploader("Upload CSV with 'video','views','likes','comments'", type='csv')
if file:
    df = load_data(file)
    st.dataframe(df.head())

    df_metrics = compute_metrics(df)
    st.dataframe(df_metrics)

    plot_metrics(df_metrics)