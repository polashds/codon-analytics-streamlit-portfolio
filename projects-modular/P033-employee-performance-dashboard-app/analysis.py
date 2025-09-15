
def compute_performance_metrics(df):
    df['efficiency'] = df['tasks_completed'] / df['hours_worked']
    df['score'] = (df['efficiency']*0.7 + df['rating']*0.3)
    return df