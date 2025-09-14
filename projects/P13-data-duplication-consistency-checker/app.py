
import pandas as pd

df = pd.read_csv('customer_data.csv')
duplicates = df[df.duplicated()]
print("Duplicate rows:\n", duplicates)
df = df.drop_duplicates()
df.to_csv('customer_data_cleaned.csv', index=False)