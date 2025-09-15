
from sklearn.ensemble import IsolationForest

def detect_anomalies(df, contamination=0.05):
    model = IsolationForest(contamination=contamination)
    df['anomaly'] = model.fit_predict(df)
    return df