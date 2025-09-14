
import streamlit as st
import pandas as pd

st.title("Data Conversion App")

file = st.file_uploader("Upload CSV/Excel", type=['csv','xlsx'])
if file:
    if file.name.endswith('.csv'):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)
    st.dataframe(df.head())

    format_choice = st.selectbox("Select Output Format", ['CSV', 'JSON'])
    if st.button("Convert"):
        if format_choice == 'CSV':
            df.to_csv('converted.csv', index=False)
            st.success("Saved as converted.csv")
        else:
            df.to_json('converted.json', orient='records')
            st.success("Saved as converted.json")