
import streamlit as st
import plotly.express as px

def plot_fraud(df):
    fig = px.scatter(df, x='amount', y='time', color='fraud', title="Transaction Fraud Detection")
    st.plotly_chart(fig)