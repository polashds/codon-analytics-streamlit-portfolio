
import streamlit as st
import plotly.express as px

def plot_patient_age_distribution(df):
    fig = px.histogram(df, x='age', nbins=20, title="Patient Age Distribution")
    st.plotly_chart(fig)