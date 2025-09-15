
import streamlit as st
from data_loader import load_data
from model import train_model, predict_rating

st.title("Item Recommendation System")

file = st.file_uploader("Upload CSV (user,item,rating)", type='csv')
if file:
    df = load_data(file)
    st.dataframe(df.head())

    user_input = st.text_input("Enter User ID")
    item_input = st.text_input("Enter Item ID")
    if st.button("Predict Rating"):
        model = train_model(df)
        rating = predict_rating(model, user_input, item_input)
        st.success(f"Predicted Rating: {rating:.2f}")