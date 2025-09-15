
from textblob import TextBlob

def analyze_sentiment(df):
    df['polarity'] = df['tweet_text'].apply(lambda x: TextBlob(x).sentiment.polarity)
    df['sentiment'] = df['polarity'].apply(lambda x: 'Positive' if x>0 else ('Negative' if x<0 else 'Neutral'))
    return df