
import streamlit as st
import plotly.express as px

def plot_performance(df):
    fig = px.bar(df, x='employee', y='score', title="Employee Performance Score")
    st.plotly_chart(fig)