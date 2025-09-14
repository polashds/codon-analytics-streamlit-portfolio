
import streamlit as st
import pandas as pd
import sqlite3

st.title("SQL Query Runner App")

uploaded_file = st.file_uploader("Upload CSV to create table", type='csv')
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    conn = sqlite3.connect("data.db")
    df.to_sql("data_table", conn, if_exists='replace', index=False)
    query = st.text_area("Write your SQL query here")
    
    if st.button("Run Query"):
        result = pd.read_sql_query(query, conn)
        st.dataframe(result)