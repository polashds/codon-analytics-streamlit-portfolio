
import streamlit as st
from transformers import pipeline

st.title("Text Summarization App")

text = st.text_area("Paste text to summarize")
if st.button("Summarize"):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
    st.write("Summary:", summary[0]['summary_text'])