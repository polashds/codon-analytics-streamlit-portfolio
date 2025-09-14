
import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('sales.csv')
st.title("KPI Dashboard")

fig = px.line(df, x='month', y='revenue', color='region')
st.plotly_chart(fig)