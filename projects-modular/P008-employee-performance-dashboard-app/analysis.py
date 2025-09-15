
def calculate_performance_score(df):
    df['performance_score'] = df[['tasks_completed','hours_worked','client_feedback']].sum(axis=1)
    return df