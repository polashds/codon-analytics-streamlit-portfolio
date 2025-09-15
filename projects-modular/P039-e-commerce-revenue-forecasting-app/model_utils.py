
from statsmodels.tsa.holtwinters import ExponentialSmoothing

def forecast_revenue(df, periods=14):
    model = ExponentialSmoothing(df['revenue'], trend='add', seasonal=None)
    model_fit = model.fit()
    forecast = model_fit.forecast(periods)
    forecast_df = df.tail(periods).copy()
    forecast_df['forecast'] = forecast.values
    return forecast_df