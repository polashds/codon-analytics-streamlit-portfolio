
import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

st.title("Simple Web Scraper")

url = st.text_input("Enter website URL (example: products page)")

if st.button("Scrape"):
    if url:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        products = []
        for item in soup.select('.product'):
            name = item.select_one('.name').text
            price = item.select_one('.price').text
            products.append({'name': name, 'price': price})
        df = pd.DataFrame(products)
        st.dataframe(df)
        df.to_csv("scraped_data.csv", index=False)
        st.success("Scraped data saved as scraped_data.csv")