
import streamlit as st
from data_utils import load_data
from analysis import compute_patient_stats
from visualizations import plot_patient_age_distribution

st.title("Hospital Patient Analytics Dashboard")

file = st.file_uploader("Upload CSV with 'patient_id','age','department','admission_date'", type='csv')
if file:
    df = load_data(file)
    st.dataframe(df.head())

    department = st.selectbox("Select Department", df['department'].unique())
    df_department = df[df['department']==department]

    stats = compute_patient_stats(df_department)
    st.write(stats)

    plot_patient_age_distribution(df_department)