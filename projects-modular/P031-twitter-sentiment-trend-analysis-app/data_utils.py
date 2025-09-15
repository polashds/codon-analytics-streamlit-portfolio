
import pandas as pd

def load_data(file):
    df = pd.read_csv(file, parse_dates=['date'])
    df.dropna(subset=['tweet_text'], inplace=True)
    return df