
def compute_occupancy_stats(df):
    df['occupancy_rate'] = df['occupied_beds'] / df['total_beds'] * 100
    return {
        'Average Occupancy Rate (%)': df['occupancy_rate'].mean(),
        'Max Occupancy Rate (%)': df['occupancy_rate'].max(),
        'Min Occupancy Rate (%)': df['occupancy_rate'].min()
    }