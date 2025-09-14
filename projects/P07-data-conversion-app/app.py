
import pandas as pd

# CSV to JSON
df = pd.read_csv('sales_data_cleaned.csv')
df.to_json('sales_data.json', orient='records')