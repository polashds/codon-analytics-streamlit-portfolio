
import streamlit as st
from data_utils import load_data
from analysis import compute_health_stats
from visualizations import plot_vitals_trends

st.title("Healthcare Patient Monitoring Dashboard")

file = st.file_uploader("Upload CSV with 'date','patient','heart_rate','blood_pressure'", type='csv')
if file:
    df = load_data(file)
    st.dataframe(df.head())

    patient = st.selectbox("Select Patient", df['patient'].unique())
    df_patient = df[df['patient']==patient]

    stats = compute_health_stats(df_patient)
    st.write(stats)

    plot_vitals_trends(df_patient)