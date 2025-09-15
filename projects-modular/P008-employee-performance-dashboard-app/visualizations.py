
import streamlit as st
import plotly.express as px

def plot_performance(df):
    fig = px.bar(df, x='employee_id', y='performance_score', color='performance_score',
                 title="Employee Performance Scores")
    st.plotly_chart(fig)