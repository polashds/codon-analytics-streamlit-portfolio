
def aggregate_consumption(df):
    return df.groupby('date')['consumption'].sum().reset_index()