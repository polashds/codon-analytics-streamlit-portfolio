
import streamlit as st
import pandas as pd

st.title("CSV/Excel Data Cleaner")

file = st.file_uploader("Upload your CSV or Excel file", type=['csv', 'xlsx'])
if file:
    if file.name.endswith('.csv'):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)
    
    st.subheader("Original Data")
    st.dataframe(df.head())

    if st.button("Clean Data"):
        df = df.drop_duplicates()
        df.fillna(df.mean(numeric_only=True), inplace=True)
        df.columns = df.columns.str.lower().str.replace(' ', '_')
        st.subheader("Cleaned Data")
        st.dataframe(df.head())
        df.to_csv("cleaned_data.csv", index=False)
        st.success("Cleaned data saved as cleaned_data.csv")