
import streamlit as st
from data_utils import load_data
from analysis import cluster_customers
from visualizations import plot_clusters

st.title("Customer Segmentation Dashboard")

file = st.file_uploader("Upload CSV with numerical features", type='csv')
if file:
    df = load_data(file)
    st.dataframe(df.head())

    n_clusters = st.slider("Number of Clusters", 2, 10, 3)
    df_clustered = cluster_customers(df, n_clusters)
    plot_clusters(df_clustered)