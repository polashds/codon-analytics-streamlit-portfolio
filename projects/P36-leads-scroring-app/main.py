
import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression

st.title("Lead Scoring App")

file = st.file_uploader("Upload CSV with leads & features", type='csv')
if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())

    features = st.multiselect("Select features", df.columns.drop('converted'))
    if st.button("Score Leads"):
        X = df[features]
        y = df['converted']
        model = LogisticRegression()
        model.fit(X, y)
        df['lead_score'] = model.predict_proba(X)[:,1]
        st.dataframe(df[['lead_score']].head())
        df.to_csv("lead_scores.csv", index=False)
        st.success("Lead scores saved!")