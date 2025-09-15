
import streamlit as st
import plotly.express as px

def plot_attrition_distribution(df):
    fig = px.histogram(df, x='predicted_attrition', title="Predicted Attrition Distribution")
    st.plotly_chart(fig)