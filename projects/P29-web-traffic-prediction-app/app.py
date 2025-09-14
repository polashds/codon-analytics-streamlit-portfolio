
from prophet import Prophet
import pandas as pd

df = pd.read_csv('web_traffic.csv')
df = df.rename(columns={'date':'ds', 'visitors':'y'})

model = Prophet()
model.fit(df)
future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)
forecast[['ds','yhat','yhat_lower','yhat_upper']].tail()