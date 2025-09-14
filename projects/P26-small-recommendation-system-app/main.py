
import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

st.title("Item Recommendation System")

file = st.file_uploader("Upload CSV with item features", type='csv')
if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())

    similarity = cosine_similarity(df.drop('item_name', axis=1))
    df_sim = pd.DataFrame(similarity, index=df['item_name'], columns=df['item_name'])

    item_input = st.selectbox("Select Item", df['item_name'])
    st.subheader(f"Top 5 similar items to {item_input}")
    st.write(df_sim[item_input].sort_values(ascending=False)[1:6])