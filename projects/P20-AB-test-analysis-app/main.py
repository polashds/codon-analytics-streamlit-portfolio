
import streamlit as st
import pandas as pd
from scipy import stats

st.title("A/B Test Analysis")

file = st.file_uploader("Upload CSV with groups A/B and conversions", type='csv')
if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())

    if st.button("Run T-test"):
        groupA = df[df['group']=='A']['conversion']
        groupB = df[df['group']=='B']['conversion']
        t_stat, p_val = stats.ttest_ind(groupA, groupB)
        st.success(f"T-statistic: {t_stat:.2f}, P-value: {p_val:.4f}")