
import streamlit as st
import pandas as pd

st.title("Text Annotation App")

uploaded_file = st.file_uploader("Upload CSV with text column", type='csv')
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df.head())
    
    annotated = []
    for idx, row in df.iterrows():
        label = st.radio(f"Label for: {row['text']}", ['Positive', 'Negative', 'Neutral'], key=idx)
        annotated.append(label)

    if st.button("Save Annotations"):
        df['label'] = annotated
        df.to_csv("annotated_data.csv", index=False)
        st.success("Annotations saved!")