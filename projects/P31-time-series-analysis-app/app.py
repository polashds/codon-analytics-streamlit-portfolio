
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

df = pd.read_csv('sales_data.csv', parse_dates=['date'], index_col='date')
result = seasonal_decompose(df['revenue'], model='additive', period=12)

result.plot()
plt.show()