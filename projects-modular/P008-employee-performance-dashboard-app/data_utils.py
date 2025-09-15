
import pandas as pd

def load_data(file):
    df = pd.read_csv(file)
    df.fillna(0, inplace=True)
    return df