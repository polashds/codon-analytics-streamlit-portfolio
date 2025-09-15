
import streamlit as st
import plotly.express as px

def plot_clusters(df):
    if df.shape[1] >= 3:
        fig = px.scatter_3d(df, x=df.columns[0], y=df.columns[1], z=df.columns[2], color='cluster', title="Customer Segments")
        st.plotly_chart(fig)
    else:
        fig = px.scatter(df, x=df.columns[0], y=df.columns[1], color='cluster', title="Customer Segments")
        st.plotly_chart(fig)