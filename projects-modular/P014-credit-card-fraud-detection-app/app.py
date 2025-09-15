
import streamlit as st
from data_utils import load_data
from model_utils import detect_fraud
from visualizations import plot_fraud

st.title("Credit Card Fraud Detection Dashboard")

file = st.file_uploader("Upload CSV with transactions", type='csv')
if file:
    df = load_data(file)
    st.dataframe(df.head())

    contamination = st.slider("Select Contamination Fraction", 0.01, 0.1, 0.02)
    if st.button("Detect Fraud"):
        df = detect_fraud(df, contamination)
        plot_fraud(df)
        st.success("Fraud detection complete")
        df.to_csv("fraud_detected.csv", index=False)