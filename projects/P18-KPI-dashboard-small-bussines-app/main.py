
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("KPI Dashboard")

file = st.file_uploader("Upload CSV", type='csv')
if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())

    kpi = st.selectbox("Select KPI", df.columns[1:])
    fig = px.line(df, x=df.columns[0], y=kpi, title=f"{kpi} over time")
    st.plotly_chart(fig)