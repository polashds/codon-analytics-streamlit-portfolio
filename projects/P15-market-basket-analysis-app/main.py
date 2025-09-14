
import streamlit as st
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

st.title("Market Basket Analysis")

file = st.file_uploader("Upload Transaction CSV", type='csv')
if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())

    min_support = st.slider("Select Minimum Support", 0.01, 0.5, 0.1)
    if st.button("Run Association Analysis"):
        frequent_itemsets = apriori(df, min_support=min_support, use_colnames=True)
        rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
        st.dataframe(rules.head())
        rules.to_csv("association_rules.csv", index=False)
        st.success("Rules saved!")