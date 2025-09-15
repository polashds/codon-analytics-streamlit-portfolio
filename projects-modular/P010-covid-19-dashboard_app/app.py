
import streamlit as st
from data_utils import load_data
from visualizations import plot_country_metric

st.title("Interactive COVID-19 Dashboard")

file = st.file_uploader("Upload CSV with 'date','country','cases','deaths'", type='csv')
if file:
    df = load_data(file)
    st.dataframe(df.head())

    country = st.selectbox("Select Country", df['country'].unique())
    metric = st.selectbox("Select Metric", ['cases','deaths'])
    plot_country_metric(df, country, metric)