
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pandas as pd

df = pd.read_csv('social_engagement.csv')
X = df[['followers','post_length','hashtags']]
y = df['likes']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestRegressor()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print(predictions[:5])