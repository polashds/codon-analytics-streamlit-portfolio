
import streamlit as st
import plotly.express as px

def plot_campaign_results(df):
    fig = px.bar(df, x='campaign', y='ROI', color='CPC', title="Marketing Campaign ROI & CPC")
    st.plotly_chart(fig)