
def compute_health_stats(df):
    return {
        'Average Heart Rate': df['heart_rate'].mean(),
        'Max Heart Rate': df['heart_rate'].max(),
        'Average Blood Pressure': df['blood_pressure'].mean(),
        'Max Blood Pressure': df['blood_pressure'].max()
    }