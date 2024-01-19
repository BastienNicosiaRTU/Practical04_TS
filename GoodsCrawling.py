import requests
from bs4 import BeautifulSoup

url = 'https://scrapeme.live/shop/'  
response = requests.get(url)
webpage_content = response.content

soup = BeautifulSoup(webpage_content, 'html.parser')


products = []
for product in soup.find_all('div', class_='content-area'):  
    product_name = product.find('h2', class_='woocommerce-loop-product__title').text.strip()  
    product_price = product.find('span', class_='price').text.strip()  
    products.append((product_name, product_price))
    

for product_name, product_price in products:
    print(f"Product: {product_name}, Price: {product_price}")

