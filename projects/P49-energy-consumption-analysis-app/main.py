
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Energy Consumption Analysis")

file = st.file_uploader("Upload CSV with 'date','consumption'", type='csv')
if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())

    fig = px.line(df, x='date', y='consumption', title="Energy Consumption Over Time")
    st.plotly_chart(fig)