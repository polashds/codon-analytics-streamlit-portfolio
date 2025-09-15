
from prophet import Prophet

def train_forecast_model(df):
    model = Prophet(daily_seasonality=True)
    model.fit(df)
    return model

def make_forecast(model, periods):
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast