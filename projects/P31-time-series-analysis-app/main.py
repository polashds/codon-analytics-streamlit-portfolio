
import streamlit as st
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt

st.title("Time Series Analysis App")

file = st.file_uploader("Upload CSV with date & value", type='csv')
if file:
    df = pd.read_csv(file, parse_dates=['date'])
    st.dataframe(df.head())

    period = st.number_input("Enter seasonal period (e.g., 12 for monthly)", min_value=1, value=12)
    if st.button("Decompose Series"):
        result = seasonal_decompose(df['value'], model='additive', period=period)
        fig, ax = plt.subplots(4,1, figsize=(10,8))
        result.observed.plot(ax=ax[0], title='Observed')
        result.trend.plot(ax=ax[1], title='Trend')
        result.seasonal.plot(ax=ax[2], title='Seasonal')
        result.resid.plot(ax=ax[3], title='Residual')
        st.pyplot(fig)