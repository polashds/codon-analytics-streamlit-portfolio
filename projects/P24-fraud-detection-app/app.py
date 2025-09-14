
from sklearn.ensemble import IsolationForest
import pandas as pd

df = pd.read_csv('transactions.csv')
model = IsolationForest(contamination=0.05)
df['anomaly'] = model.fit_predict(df[['amount', 'transaction_time']])
anomalies = df[df['anomaly']==-1]
anomalies.to_csv('fraudulent_transactions.csv', index=False)