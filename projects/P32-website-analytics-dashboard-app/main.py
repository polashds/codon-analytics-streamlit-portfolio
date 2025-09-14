
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Website Analytics Dashboard")

file = st.file_uploader("Upload CSV with 'source' & 'visits'", type='csv')
if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())

    fig = px.bar(df, x='source', y='visits', title="Visits by Source")
    st.plotly_chart(fig)

    fig2 = px.line(df, x='date', y='visits', color='source', title="Traffic Trend")
    st.plotly_chart(fig2)