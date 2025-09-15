
import streamlit as st
from data_utils import load_data
from model_utils import train_model, predict_attrition
from visualizations import plot_attrition_distribution

st.title("Employee Attrition Prediction Dashboard")

file = st.file_uploader("Upload CSV with employee features", type='csv')
if file:
    df = load_data(file)
    st.dataframe(df.head())

    if st.button("Train Model"):
        model = train_model(df)
        df['predicted_attrition'] = df.apply(lambda row: predict_attrition(model, row), axis=1)
        st.dataframe(df[['employee_id','predicted_attrition']])
        plot_attrition_distribution(df)