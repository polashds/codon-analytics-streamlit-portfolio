
import pandas as pd

df = pd.read_csv('reviews.csv')
# Example: label sentiment manually
df['sentiment'] = df['review'].apply(lambda x: 'positive' if 'good' in x else 'negative')
df.to_csv('labeled_reviews.csv', index=False)