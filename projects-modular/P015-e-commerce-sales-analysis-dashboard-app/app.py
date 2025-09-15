
import streamlit as st
from data_utils import load_data
from analysis import aggregate_sales
from visualizations import plot_sales

st.title("E-commerce Sales Analysis Dashboard")

file = st.file_uploader("Upload CSV with 'date','product','sales'", type='csv')
if file:
    df = load_data(file)
    st.dataframe(df.head())

    aggregated_df = aggregate_sales(df)
    plot_sales(aggregated_df)