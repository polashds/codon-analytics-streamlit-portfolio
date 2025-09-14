
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Survey Data Analysis App")

file = st.file_uploader("Upload CSV with survey responses", type='csv')
if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())

    col = st.selectbox("Select column to analyze", df.columns)
    if st.button("Plot Survey Distribution"):
        fig, ax = plt.subplots()
        sns.countplot(x=col, data=df, ax=ax)
        st.pyplot(fig)