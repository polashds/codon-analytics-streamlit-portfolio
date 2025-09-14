
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

st.title("Loan Approval Prediction")

file = st.file_uploader("Upload CSV with features & approval", type='csv')
if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())

    features = st.multiselect("Select features", df.columns.drop('approved'))
    if st.button("Train Model"):
        X = df[features]
        y = df['approved']
        model = RandomForestClassifier()
        model.fit(X, y)
        st.success("Model trained")
        st.write("Predictions for first 5 rows:", model.predict(X.head()))
