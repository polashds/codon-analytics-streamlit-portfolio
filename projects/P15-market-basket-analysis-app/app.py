
from mlxtend.frequent_patterns import apriori, association_rules

basket = pd.read_csv('transactions.csv')
frequent_itemsets = apriori(basket, min_support=0.1, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
print(rules.head())