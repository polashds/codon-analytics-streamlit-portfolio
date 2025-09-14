
from textblob import TextBlob
import pandas as pd

df = pd.read_csv('reviews.csv')
df['sentiment'] = df['review'].apply(lambda x: TextBlob(x).sentiment.polarity)
print(df.head())