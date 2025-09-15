
def compute_price_stats(df):
    return {
        'Average Price': df['price'].mean(),
        'Median Price': df['price'].median(),
        'Max Price': df['price'].max(),
        'Min Price': df['price'].min()
    }