
import streamlit as st
import pandas as pd
from sklearn.ensemble import IsolationForest

st.title("Fraud Detection in Transactions")

file = st.file_uploader("Upload CSV with transactions", type='csv')
if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())

    if st.button("Detect Anomalies"):
        model = IsolationForest(contamination=0.05)
        df['anomaly'] = model.fit_predict(df[['amount', 'transaction_time']])
        st.dataframe(df[df['anomaly']==-1])
        df.to_csv("fraud_detected.csv", index=False)
        st.success("Anomalies detected and saved")