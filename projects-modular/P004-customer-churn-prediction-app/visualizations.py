
import streamlit as st
import plotly.express as px

def plot_churn_distribution(df):
    fig = px.histogram(df, x='predicted_churn', title="Predicted Churn Distribution")
    st.plotly_chart(fig)