
import streamlit as st
import plotly.graph_objects as go

def plot_vitals_trends(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['date'], y=df['heart_rate'], mode='lines+markers', name='Heart Rate'))
    fig.add_trace(go.Scatter(x=df['date'], y=df['blood_pressure'], mode='lines+markers', name='Blood Pressure'))
    fig.update_layout(title="Vitals Over Time")
    st.plotly_chart(fig)