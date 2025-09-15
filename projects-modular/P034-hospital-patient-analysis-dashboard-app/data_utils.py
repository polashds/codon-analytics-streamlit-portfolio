
import pandas as pd

def load_data(file):
    df = pd.read_csv(file, parse_dates=['admission_date'])
    df.dropna(inplace=True)
    return df