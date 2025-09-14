
import streamlit as st
import pandas as pd
from gensim import corpora, models

st.title("Topic Modeling App")

file = st.file_uploader("Upload CSV with text column", type='csv')
if file:
    df = pd.read_csv(file)
    st.dataframe(df.head())

    n_topics = st.slider("Select number of topics", 2, 10, 3)
    if st.button("Run Topic Modeling"):
        texts = [doc.split() for doc in df['text']]
        dictionary = corpora.Dictionary(texts)
        corpus = [dictionary.doc2bow(text) for text in texts]
        lda = models.LdaModel(corpus, num_topics=n_topics, id2word=dictionary, passes=10)
        topics = lda.print_topics()
        for t in topics:
            st.write(t)