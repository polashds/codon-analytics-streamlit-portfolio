
import streamlit as st
import pandas as pd
from sklearn.ensemble import IsolationForest

st.title("Credit Card Fraud Detection")

file = st.file_uploader("Upload CSV with transactions", type='csv')
if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())

    contamination = st.slider("Contamination fraction", 0.01, 0.1, 0.02)
    if st.button("Detect Fraud"):
        model = IsolationForest(contamination=contamination)
        df['fraud'] = model.fit_predict(df)
        st.dataframe(df[df['fraud']==-1])
        df.to_csv("fraud_detected.csv", index=False)
        st.success("Fraud detection complete & saved")
