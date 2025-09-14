
import pandas as pd
from gensim import corpora, models

df = pd.read_csv('documents.csv')
texts = [doc.split() for doc in df['text']]
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
lda = models.LdaModel(corpus, num_topics=3, id2word=dictionary, passes=10)
print(lda.print_topics())