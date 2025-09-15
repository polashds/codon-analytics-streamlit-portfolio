
def aggregate_sales(df):
    return df.groupby('date')['sales'].sum().reset_index()