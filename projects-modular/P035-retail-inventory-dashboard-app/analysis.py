
def compute_inventory_stats(df):
    return {
        'Total Products': df.shape[0],
        'Total Stock': df['stock_level'].sum(),
        'Average Stock per Product': df['stock_level'].mean(),
        'Max Stock': df['stock_level'].max(),
        'Min Stock': df['stock_level'].min()
    }