
df['total_spent'] = df.groupby('customer_id')['purchase_amount'].transform('sum')
clv = df[['customer_id', 'total_spent']].drop_duplicates()
print(clv.head())