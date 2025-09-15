
import pandas as pd

def load_data(file):
    df = pd.read_csv(file, parse_dates=['date'])
    df = df.rename(columns={'date':'ds','sales':'y'})
    return df