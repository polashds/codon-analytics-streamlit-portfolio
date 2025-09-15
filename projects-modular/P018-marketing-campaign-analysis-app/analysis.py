
def compute_campaign_metrics(df):
    df['CPC'] = df['spend'] / df['conversions']
    df['ROI'] = (df['conversions']*100 - df['spend']) / df['spend']
    return df