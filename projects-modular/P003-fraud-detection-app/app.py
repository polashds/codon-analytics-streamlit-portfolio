
import streamlit as st
from data_utils import load_data
from model_utils import detect_anomalies
from visualizations import plot_anomalies

st.title("Transaction Fraud Detection Dashboard")

file = st.file_uploader("Upload CSV", type='csv')
if file:
    df = load_data(file)
    st.dataframe(df.head())

    contamination = st.slider("Select Contamination Fraction", 0.01, 0.1, 0.02)
    if st.button("Detect Fraud"):
        df = detect_anomalies(df, contamination)
        plot_anomalies(df)
        df.to_csv("fraud_detected.csv", index=False)
        st.success("Fraud detection complete & saved")