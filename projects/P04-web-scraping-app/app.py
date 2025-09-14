
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://example.com/products'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

products = []
for item in soup.select('.product'):
    name = item.select_one('.name').text
    price = item.select_one('.price').text
    products.append({'name': name, 'price': price})

df = pd.DataFrame(products)
df.to_csv('products.csv', index=False)