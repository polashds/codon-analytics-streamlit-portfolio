
import pandas as pd
import seaborn as sns

df = pd.read_csv('survey.csv')
sns.countplot(x='satisfaction', data=df)