
import streamlit as st
from data_utils import load_data
from model_utils import train_model, predict_default
from visualizations import plot_default_distribution

st.title("Loan Default Prediction Dashboard")

file = st.file_uploader("Upload CSV with loan applicant features", type='csv')
if file:
    df = load_data(file)
    st.dataframe(df.head())

    if st.button("Train Model"):
        model = train_model(df)
        df['predicted_default'] = df.apply(lambda row: predict_default(model, row), axis=1)
        st.dataframe(df[['applicant_id','predicted_default']])
        plot_default_distribution(df)