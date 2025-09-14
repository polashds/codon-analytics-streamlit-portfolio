
from sklearn.cluster import KMeans
import pandas as pd
import seaborn as sns

df = pd.read_csv('customers.csv')
kmeans = KMeans(n_clusters=3)
df['segment'] = kmeans.fit_predict(df[['age','spending_score']])
sns.scatterplot(x='age', y='spending_score', hue='segment', data=df)