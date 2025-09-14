
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Social Media Analytics Dashboard")

file = st.file_uploader("Upload Social Media CSV", type='csv')
if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())

    metric = st.selectbox("Select metric", ['likes','comments','shares'])
    fig = px.bar(df, x='post_type', y=metric, color='post_type', title=f"{metric.title()} by Post Type")
    st.plotly_chart(fig)