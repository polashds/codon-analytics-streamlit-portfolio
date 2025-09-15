
def compute_accident_stats(df):
    return {
        'Total Accidents': df['accidents'].sum(),
        'Total Fatalities': df['fatalities'].sum(),
        'Average Accidents per Day': df['accidents'].mean()
    }