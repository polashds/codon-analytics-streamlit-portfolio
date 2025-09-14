
import streamlit as st
import pandas as pd
from sklearn.ensemble import IsolationForest

st.title("Anomaly Detection App")

file = st.file_uploader("Upload CSV with features", type='csv')
if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())

    contamination = st.slider("Select contamination fraction", 0.01, 0.2, 0.05)
    if st.button("Detect Anomalies"):
        model = IsolationForest(contamination=contamination)
        df['anomaly'] = model.fit_predict(df)
        st.dataframe(df[df['anomaly']==-1])
        df.to_csv("anomalies.csv", index=False)
        st.success("Anomalies detected & saved")