
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

st.title("Predictive Modeling App")

file = st.file_uploader("Upload CSV", type='csv')
if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())

    features = st.multiselect("Select Features", df.columns.tolist())
    target = st.selectbox("Select Target Column", df.columns.tolist())

    if st.button("Train Model"):
        X = df[features]
        y = df[target]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        model = LinearRegression()
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        st.write("Predictions:", predictions[:5])
        st.success("Model trained successfully!")