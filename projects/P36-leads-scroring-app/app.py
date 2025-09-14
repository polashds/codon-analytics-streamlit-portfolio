
from sklearn.linear_model import LogisticRegression
import pandas as pd

df = pd.read_csv('leads.csv')
X = df[['email_clicks','website_visits']]
y = df['converted']

model = LogisticRegression()
model.fit(X, y)
df['lead_score'] = model.predict_proba(X)[:,1]
df.to_csv('leads_scored.csv', index=False)