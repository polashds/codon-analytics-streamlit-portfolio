
import streamlit as st
import pandas as pd
import glob

st.title("CSV Merge Automation App")

files = st.file_uploader("Upload multiple CSV files", type='csv', accept_multiple_files=True)
if files:
    df_list = [pd.read_csv(f) for f in files]
    merged_df = pd.concat(df_list)
    st.dataframe(merged_df.head())

    if st.button("Save Merged CSV"):
        merged_df.to_csv("merged_data.csv", index=False)
        st.success("Merged data saved as merged_data.csv")