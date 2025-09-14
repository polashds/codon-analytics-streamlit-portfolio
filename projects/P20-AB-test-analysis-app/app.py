
from scipy import stats
import pandas as pd

df = pd.read_csv('ab_test.csv')
groupA = df[df['group']=='A']['conversion']
groupB = df[df['group']=='B']['conversion']

t_stat, p_val = stats.ttest_ind(groupA, groupB)
print("T-statistic:", t_stat, "P-value:", p_val)