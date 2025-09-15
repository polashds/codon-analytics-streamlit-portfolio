
import streamlit as st
from data_utils import load_data
from analysis import compute_inventory_stats
from visualizations import plot_inventory_levels

st.title("Retail Inventory Dashboard")

file = st.file_uploader("Upload CSV with 'product','category','stock_level'", type='csv')
if file:
    df = load_data(file)
    st.dataframe(df.head())

    category = st.selectbox("Select Category", df['category'].unique())
    df_category = df[df['category']==category]

    stats = compute_inventory_stats(df_category)
    st.write(stats)

    plot_inventory_levels(df_category)