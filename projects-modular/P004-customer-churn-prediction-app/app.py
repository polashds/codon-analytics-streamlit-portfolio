
import streamlit as st
from data_utils import load_data
from model_utils import train_churn_model, predict_churn
from visualizations import plot_churn_distribution

st.title("Customer Churn Prediction Dashboard")

file = st.file_uploader("Upload CSV", type='csv')
if file:
    df = load_data(file)
    st.dataframe(df.head())

    features = st.multiselect("Select Features", df.columns.drop('churn'))
    if st.button("Train Model"):
        model = train_churn_model(df, features)
        st.success("Model trained successfully")

        st.subheader("Churn Predictions")
        df['predicted_churn'] = df.apply(lambda row: predict_churn(model, row, features), axis=1)
        st.dataframe(df[['customer_id','predicted_churn']])

        plot_churn_distribution(df)