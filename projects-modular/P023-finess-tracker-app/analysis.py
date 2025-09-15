
def compute_metrics(df, metrics):
    return df[['date'] + metrics]