
import requests
from bs4 import BeautifulSoup
import pandas as pd

keywords = ['data science', 'machine learning']
results = []

for kw in keywords:
    r = requests.get(f'https://www.example.com/search?q={kw}')
    soup = BeautifulSoup(r.text, 'html.parser')
    count = int(soup.select_one('.result-count').text.split()[0])
    results.append({'keyword': kw, 'search_results': count})

df = pd.DataFrame(results)
df.to_csv('keyword_analysis.csv', index=False)