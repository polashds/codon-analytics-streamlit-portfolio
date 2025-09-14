
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Sales Dashboard")

file = st.file_uploader("Upload CSV file", type='csv')
if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())

    fig = px.bar(df, x='month', y='revenue', color='region', title="Revenue by Region")
    st.plotly_chart(fig)

    fig2 = px.line(df, x='month', y='revenue', color='region', title="Revenue Trend")
    st.plotly_chart(fig2)