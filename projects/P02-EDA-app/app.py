
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('sales_data_cleaned.csv')

# Basic statistics
print(df.describe())

# Correlation heatmap
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()

# Distribution of revenue
sns.histplot(df['revenue'], kde=True)
plt.show()