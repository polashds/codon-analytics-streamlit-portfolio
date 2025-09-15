
from sklearn.ensemble import RandomForestClassifier

def train_churn_model(df, features):
    X = df[features]
    y = df['churn']
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

def predict_churn(model, row, features):
    X = row[features].values.reshape(1, -1)
    return model.predict(X)[0]