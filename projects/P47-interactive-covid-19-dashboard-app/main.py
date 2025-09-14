
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("COVID-19 Dashboard")

file = st.file_uploader("Upload CSV with 'date','country','cases','deaths'", type='csv')
if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())

    country = st.selectbox("Select Country", df['country'].unique())
    metric = st.selectbox("Select Metric", ['cases','deaths'])
    fig = px.line(df[df['country']==country], x='date', y=metric, title=f"{metric.title()} in {country}")
    st.plotly_chart(fig)