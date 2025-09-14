
import streamlit as st
import pandas as pd
import re

st.title("Email Data Extraction")

file = st.file_uploader("Upload CSV with emails", type='csv')
if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())

    if st.button("Extract Amounts"):
        df['total_amount'] = df['email_body'].apply(lambda x: re.search(r'Total:\s*\$([0-9\.]+)', x).group(1) if re.search(r'Total:\s*\$([0-9\.]+)', x) else None)
        st.dataframe(df.head())
        df.to_csv("extracted_email_data.csv", index=False)
        st.success("Data extracted and saved")