
import streamlit as st
from utils import summarize_text
from transformers import pipeline

st.title("Interactive Text Summarization Dashboard")

text_input = st.text_area("Paste your text here")
if st.button("Summarize"):
    summary = summarize_text(text_input)
    st.subheader("Summary:")
    st.write(summary)