
import pandas as pd

def load_data(file):
    df = pd.read_csv(file)
    return df

def clean_data(df):
    df.dropna(inplace=True)
    df['post_type'] = df['post_type'].astype(str)
    return df