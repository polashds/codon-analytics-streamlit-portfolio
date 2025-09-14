
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Interactive EDA App")

file = st.file_uploader("Upload CSV", type='csv')
if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())

    st.subheader("Summary Statistics")
    st.write(df.describe())

    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    col = st.selectbox("Select column to plot distribution", numeric_cols)
    if col:
        fig, ax = plt.subplots()
        sns.histplot(df[col], kde=True, ax=ax)
        st.pyplot(fig)

    st.subheader("Correlation Heatmap")
    fig, ax = plt.subplots()
    sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)