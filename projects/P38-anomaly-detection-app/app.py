
from sklearn.ensemble import IsolationForest
import pandas as pd

df = pd.read_csv('sensor_data.csv')
model = IsolationForest(contamination=0.05)
df['anomaly'] = model.fit_predict(df[['reading1','reading2']])
df[df['anomaly']==-1].to_csv('anomalies.csv', index=False)