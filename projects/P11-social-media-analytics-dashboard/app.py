
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('social_data.csv')
sns.barplot(x='post_type', y='engagement', data=df)
plt.title("Engagement by Post Type")
plt.show()