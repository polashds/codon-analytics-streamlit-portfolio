
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('web_traffic.csv')
df.groupby('source')['visits'].sum().plot(kind='bar')
plt.title("Visits by Source")
plt.show()