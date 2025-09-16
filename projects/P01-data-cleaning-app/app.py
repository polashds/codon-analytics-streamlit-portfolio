
import pandas as pd

# Load dataset
df = pd.read_csv(r'E:\DS-Contractor\microgigs\codon-analytics-streamlit-portfolio\projects\P01-data-cleaning-app\sales_data.csv')

# Drop duplicates
df = df.drop_duplicates()

# Fill missing values
df['Revenue'] = df['Revenue'].fillna(df['Revenue'].mean())

# Standardize column names
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Save cleaned dataset
df.to_csv('sales_data_cleaned.csv', index=False)