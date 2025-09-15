
def compute_portfolio_returns(df):
    df = df.sort_values(by=['symbol','date'])
    df['daily_return'] = df.groupby('symbol')['closing_price'].pct_change()
    df['portfolio_value'] = df['closing_price'] * df['shares']
    return df