
import streamlit as st
import pandas as pd

st.title("Duplicate and Consistency Checker")

file = st.file_uploader("Upload CSV", type='csv')
if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())

    if st.button("Check Duplicates"):
        duplicates = df[df.duplicated()]
        st.write("Duplicate Rows:")
        st.dataframe(duplicates)
        st.success(f"Found {len(duplicates)} duplicates")

    if st.button("Clean Data"):
        df = df.drop_duplicates()
        df.fillna(method='ffill', inplace=True)
        st.dataframe(df.head())
        df.to_csv("cleaned_data.csv", index=False)
        st.success("Cleaned data saved!")