
import streamlit as st
import plotly.express as px

def plot_consumption(df, appliance):
    fig = px.line(df, x='date', y='consumption', title=f"{appliance} Energy Consumption Over Time")
    st.plotly_chart(fig)