
from sklearn.ensemble import RandomForestClassifier

def train_model(df):
    X = df.drop(['applicant_id','default'], axis=1)
    y = df['default']
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

def predict_default(model, row):
    X = row.drop(['applicant_id','default']).values.reshape(1, -1)
    return model.predict(X)[0]