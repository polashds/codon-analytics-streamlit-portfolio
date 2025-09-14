
import pandas as pd
from openpyxl import Workbook

df = pd.read_csv('sales_data.csv')
summary = df.groupby('region')['revenue'].sum().reset_index()

wb = Workbook()
ws = wb.active
for r in dataframe_to_rows(summary, index=False, header=True):
    ws.append(r)
wb.save('summary_report.xlsx')