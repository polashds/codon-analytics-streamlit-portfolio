
import streamlit as st
from data_utils import load_data
from analysis import compute_engagement
from visualizations import plot_engagement

st.title("Social Media Engagement Dashboard")

file = st.file_uploader("Upload CSV with 'post','likes','shares','comments'", type='csv')
if file:
    df = load_data(file)
    st.dataframe(df.head())

    df = compute_engagement(df)
    st.dataframe(df[['post','engagement_rate']])
    plot_engagement(df)