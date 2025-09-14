
from textblob import TextBlob
import pandas as pd

df = pd.read_csv('tweets.csv')
df['sentiment'] = df['text'].apply(lambda x: TextBlob(x).sentiment.polarity)
df['sentiment_label'] = df['sentiment'].apply(lambda x: 'positive' if x>0 else ('negative' if x<0 else 'neutral'))
df.to_csv('tweets_sentiment.csv', index=False)