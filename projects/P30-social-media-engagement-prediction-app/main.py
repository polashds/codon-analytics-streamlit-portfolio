
import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

st.title("Social Media Engagement Prediction")

file = st.file_uploader("Upload CSV with features & likes", type='csv')
if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())

    features = st.multiselect("Select features", df.columns.drop('likes'))
    if st.button("Train Model"):
        X = df[features]
        y = df['likes']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        model = RandomForestRegressor()
        model.fit(X_train, y_train)
        st.success("Model trained")
        st.write("Predictions for first 5 rows:")
        st.write(model.predict(X_test)[:5])