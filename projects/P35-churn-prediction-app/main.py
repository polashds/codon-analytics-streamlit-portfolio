
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

st.title("Customer Churn Prediction App")

file = st.file_uploader("Upload CSV with features & churn", type='csv')
if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())

    features = st.multiselect("Select features", df.columns.drop('churn'))
    if st.button("Train Model"):
        X = df[features]
        y = df['churn']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        model = RandomForestClassifier()
        model.fit(X_train, y_train)
        st.success("Model trained")
        st.write("Predictions for first 5 rows:", model.predict(X_test)[:5])