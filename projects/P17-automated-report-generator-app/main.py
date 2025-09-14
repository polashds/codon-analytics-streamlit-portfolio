
import streamlit as st
import pandas as pd

st.title("Automated Report Generator")

file = st.file_uploader("Upload CSV", type='csv')
if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())

    report_name = st.text_input("Enter report file name", "report.xlsx")
    if st.button("Generate Report"):
        df_summary = df.describe()
        df_summary.to_excel(report_name)
        st.success(f"Report saved as {report_name}")