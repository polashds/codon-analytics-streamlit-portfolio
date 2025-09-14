
import streamlit as st
import pandas as pd

st.title("Customer Lifetime Value (CLV) Calculator")

file = st.file_uploader("Upload Transaction CSV", type='csv')
if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())

    if st.button("Calculate CLV"):
        df['total_spent'] = df.groupby('customer_id')['purchase_amount'].transform('sum')
        clv = df[['customer_id','total_spent']].drop_duplicates()
        st.dataframe(clv.head())
        clv.to_csv("clv_report.csv", index=False)
        st.success("CLV report saved!")