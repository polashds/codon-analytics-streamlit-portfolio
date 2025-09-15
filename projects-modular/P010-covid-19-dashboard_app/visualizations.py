
import streamlit as st
import plotly.express as px

def plot_country_metric(df, country, metric):
    country_df = df[df['country']==country]
    fig = px.line(country_df, x='date', y=metric, title=f"{metric.title()} in {country}")
    st.plotly_chart(fig)