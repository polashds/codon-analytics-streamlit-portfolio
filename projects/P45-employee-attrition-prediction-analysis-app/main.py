
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

st.title("Employee Attrition Prediction")

file = st.file_uploader("Upload CSV with features & attrition", type='csv')
if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())

    features = st.multiselect("Select features", df.columns.drop('attrition'))
    if st.button("Train Model"):
        X = df[features]
        y = df['attrition']
        model = RandomForestClassifier()
        model.fit(X, y)
        st.success("Model trained")
        st.write("Predictions for first 5 rows:", model.predict(X.head()))
