
from transformers import pipeline

summarizer = pipeline("summarization")
text = open('article.txt').read()
summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
print(summary[0]['summary_text'])