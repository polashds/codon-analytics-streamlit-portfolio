
import streamlit as st
from data_utils import load_data
from model_utils import detect_fraud
from visualizations import plot_fraud

st.title("Fraudulent Transaction Detection Dashboard")

file = st.file_uploader("Upload CSV with 'amount','time','transaction_type'", type='csv')
if file:
    df = load_data(file)
    st.dataframe(df.head())

    contamination = st.slider("Anomaly Detection Contamination", 0.01, 0.1, 0.02)
    df = detect_fraud(df, contamination)
    st.dataframe(df[['amount','transaction_type','fraud']])

    plot_fraud(df)
