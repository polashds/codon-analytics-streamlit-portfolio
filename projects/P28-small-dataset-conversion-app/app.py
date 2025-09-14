
import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('sales_data.csv')
engine = create_engine('sqlite:///sales.db')
df.to_sql('sales', engine, index=False, if_exists='replace')