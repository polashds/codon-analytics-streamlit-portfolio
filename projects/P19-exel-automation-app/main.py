
import streamlit as st
import pandas as pd

st.title("Merge Multiple CSVs")

uploaded_files = st.file_uploader("Upload CSVs", type='csv', accept_multiple_files=True)
if uploaded_files:
    df_list = [pd.read_csv(f) for f in uploaded_files]
    merged_df = pd.concat(df_list)
    st.dataframe(merged_df.head())

    if st.button("Download Merged CSV"):
        merged_df.to_csv("merged_data.csv", index=False)
        st.success("Merged CSV saved!")