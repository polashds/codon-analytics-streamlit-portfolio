
import streamlit as st
import plotly.express as px

def engagement_bar_chart(df, metric):
    fig = px.bar(df, x='post_type', y=metric, color='post_type',
                 title=f"{metric.title()} by Post Type")
    st.plotly_chart(fig, use_container_width=True)