
import pandas as pd

def load_data(file):
    df = pd.read_csv(file)
    df.dropna(inplace=True)
    return df