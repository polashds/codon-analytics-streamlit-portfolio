
import requests
from bs4 import BeautifulSoup
import pandas as pd

urls = ['https://example.com/product1', 'https://example.com/product2']
prices = []

for url in urls:
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    price = soup.select_one('.price').text
    prices.append(price)

df = pd.DataFrame({'product_url': urls, 'price': prices})
df.to_csv('price_comparison.csv', index=False)