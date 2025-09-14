
import pandas as pd
import seaborn as sns

df = pd.read_csv('market_data.csv')
sns.lineplot(x='date', y='price', hue='product', data=df)