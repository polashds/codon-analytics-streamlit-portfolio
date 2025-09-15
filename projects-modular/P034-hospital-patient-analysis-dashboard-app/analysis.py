
def compute_patient_stats(df):
    return {
        'Total Patients': df.shape[0],
        'Average Age': df['age'].mean(),
        'Max Age': df['age'].max(),
        'Min Age': df['age'].min()
    }