
import streamlit as st
import plotly.express as px

def plot_occupancy_trend(df):
    df['occupancy_rate'] = df['occupied_beds'] / df['total_beds'] * 100
    fig = px.line(df, x='date', y='occupancy_rate', title="Bed Occupancy Rate Over Time")
    st.plotly_chart(fig)