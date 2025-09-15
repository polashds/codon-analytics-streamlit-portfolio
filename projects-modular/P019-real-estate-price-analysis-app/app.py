
import streamlit as st
from data_utils import load_data
from analysis import compute_price_stats
from visualizations import plot_price_distribution

st.title("Real Estate Price Analysis Dashboard")

file = st.file_uploader("Upload CSV with 'location','price','size'", type='csv')
if file:
    df = load_data(file)
    st.dataframe(df.head())

    location = st.selectbox("Select Location", df['location'].unique())
    df_location = df[df['location']==location]

    stats = compute_price_stats(df_location)
    st.write(stats)

    plot_price_distribution(df_location)