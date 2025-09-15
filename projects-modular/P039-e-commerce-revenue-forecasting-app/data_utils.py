
import pandas as pd

def load_data(file):
    df = pd.read_csv(file, parse_dates=['date'])
    df = df.sort_values('date')
    df.dropna(inplace=True)
    return df