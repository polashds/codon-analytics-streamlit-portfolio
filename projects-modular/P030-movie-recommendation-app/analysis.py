
def compute_engagement(df):
    df['engagement_rate'] = (df['likes'] + df['shares'] + df['comments']) / 100  # simplified
    return df