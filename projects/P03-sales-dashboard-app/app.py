
import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('sales_data_cleaned.csv')

st.title("Sales Dashboard")

fig = px.bar(df, x='month', y='revenue', color='region')
st.plotly_chart(fig)