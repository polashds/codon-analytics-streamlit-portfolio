
import streamlit as st
import plotly.express as px

def plot_default_distribution(df):
    fig = px.histogram(df, x='predicted_default', title="Predicted Loan Default Distribution")
    st.plotly_chart(fig)