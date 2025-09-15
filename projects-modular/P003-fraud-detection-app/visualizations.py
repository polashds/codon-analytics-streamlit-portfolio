
import streamlit as st
import plotly.express as px

def plot_anomalies(df):
    fig = px.scatter(df, x='transaction_amount', y='transaction_time', color='anomaly',
                     title="Transaction Anomalies")
    st.plotly_chart(fig)