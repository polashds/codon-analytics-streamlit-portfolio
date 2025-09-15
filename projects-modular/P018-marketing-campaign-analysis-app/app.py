
import streamlit as st
from data_utils import load_data
from analysis import compute_campaign_metrics
from visualizations import plot_campaign_results

st.title("Marketing Campaign Analysis Dashboard")

file = st.file_uploader("Upload CSV with 'campaign','spend','conversions'", type='csv')
if file:
    df = load_data(file)
    st.dataframe(df.head())

    df_metrics = compute_campaign_metrics(df)
    st.dataframe(df_metrics)

    plot_campaign_results(df_metrics)