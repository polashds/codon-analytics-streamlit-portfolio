
def compute_returns(df):
    df = df.sort_values(by=['symbol','date'])
    df['return'] = df.groupby('symbol')['close'].pct_change()
    return df