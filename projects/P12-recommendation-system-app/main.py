
import streamlit as st
import pandas as pd
from surprise import Dataset, SVD, Reader

st.title("Simple Recommendation System")

file = st.file_uploader("Upload CSV with user-item-rating", type='csv')
if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())

    reader = Reader(rating_scale=(df['rating'].min(), df['rating'].max()))
    data = Dataset.load_from_df(df[['user_id','item_id','rating']], reader)
    trainset = data.build_full_trainset()

    model = SVD()
    model.fit(trainset)

    user_input = st.text_input("Enter User ID")
    item_input = st.text_input("Enter Item ID")
    if st.button("Predict Rating"):
        pred = model.predict(user_input, item_input)
        st.success(f"Predicted Rating: {pred.est:.2f}")