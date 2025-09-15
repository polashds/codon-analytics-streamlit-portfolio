
from sklearn.ensemble import IsolationForest

def detect_fraud(df, contamination=0.05):
    model = IsolationForest(contamination=contamination, random_state=42)
    df['fraud'] = model.fit_predict(df)
    return df