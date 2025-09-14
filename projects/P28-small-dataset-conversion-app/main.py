
import streamlit as st
import pandas as pd

st.title("Dataset Conversion App")

file = st.file_uploader("Upload CSV/Excel", type=['csv','xlsx'])
if file:
    if file.name.endswith('.csv'):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)
    st.dataframe(df.head())

    format_choice = st.selectbox("Select output format", ['CSV','JSON','Excel'])
    if st.button("Convert"):
        if format_choice == 'CSV':
            df.to_csv("converted.csv", index=False)
        elif format_choice == 'JSON':
            df.to_json("converted.json", orient='records')
        else:
            df.to_excel("converted.xlsx", index=False)
        st.success(f"File converted to {format_choice}")