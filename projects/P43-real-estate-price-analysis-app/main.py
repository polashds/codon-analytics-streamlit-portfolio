
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Real Estate Price Analysis")

file = st.file_uploader("Upload CSV with 'location', 'price'", type='csv')
if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())

    loc = st.selectbox("Select Location", df['location'].unique())
    fig = px.histogram(df[df['location']==loc], x='price', title=f"Price Distribution in {loc}")
    st.plotly_chart(fig)