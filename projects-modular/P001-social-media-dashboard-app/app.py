python
import streamlit as st
from data_processing import load_data, clean_data
from visualizations import engagement_bar_chart

st.set_page_config(page_title="Social Media Dashboard", layout="wide")
st.title("Social Media Analytics Dashboard")

file = st.file_uploader("Upload CSV", type='csv')
if file:
    df = load_data(file)
    df = clean_data(df)
    st.dataframe(df.head())

    metric = st.selectbox("Select metric", ['likes','comments','shares'])
    engagement_bar_chart(df, metric)