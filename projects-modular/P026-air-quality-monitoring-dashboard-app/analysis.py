
def compute_aqi(df):
    # Simplified AQI calculation using PM2.5 and PM10
    df['AQI'] = df[['pm2.5','pm10']].mean(axis=1)
    return df