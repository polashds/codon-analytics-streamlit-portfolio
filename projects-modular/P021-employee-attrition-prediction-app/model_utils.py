
from sklearn.ensemble import RandomForestClassifier

def train_model(df):
    X = df.drop(['employee_id','attrition'], axis=1)
    y = df['attrition']
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

def predict_attrition(model, row):
    X = row.drop(['employee_id','attrition']).values.reshape(1, -1)
    return model.predict(X)[0]