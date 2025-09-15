
import streamlit as st
import plotly.express as px

def plot_energy_trend(df):
    fig = px.line(df, x='date', y='consumption', title="Energy Consumption Over Time")
    st.plotly_chart(fig)