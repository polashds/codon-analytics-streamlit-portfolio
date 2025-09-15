
def compute_metrics(df):
    df['engagement_rate'] = (df['likes'] + df['comments']) / df['views']
    return df