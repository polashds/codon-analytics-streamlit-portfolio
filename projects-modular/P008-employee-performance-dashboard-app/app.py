
import streamlit as st
from data_utils import load_data
from analysis import calculate_performance_score
from visualizations import plot_performance

st.title("Employee Performance Dashboard")

file = st.file_uploader("Upload CSV with employee data", type='csv')
if file:
    df = load_data(file)
    st.dataframe(df.head())

    df = calculate_performance_score(df)
    st.dataframe(df[['employee_id','performance_score']].sort_values(by='performance_score', ascending=False))

    plot_performance(df)