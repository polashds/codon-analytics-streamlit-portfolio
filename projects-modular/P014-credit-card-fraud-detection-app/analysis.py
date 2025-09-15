
import pandas as pd

def load_stock_data(file):
    df = pd.read_csv(file, parse_dates=['date'])
    df.dropna(inplace=True)
    return df