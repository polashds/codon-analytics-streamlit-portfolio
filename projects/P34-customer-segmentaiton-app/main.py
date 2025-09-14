
import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Customer Segmentation App")

file = st.file_uploader("Upload CSV with 'age' & 'spending_score'", type='csv')
if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())

    n_clusters = st.slider("Select number of clusters", 2, 10, 3)
    if st.button("Segment Customers"):
        kmeans = KMeans(n_clusters=n_clusters)
        df['segment'] = kmeans.fit_predict(df[['age','spending_score']])
        fig, ax = plt.subplots()
        sns.scatterplot(x='age', y='spending_score', hue='segment', data=df, ax=ax, palette='Set2')
        st.pyplot(fig)