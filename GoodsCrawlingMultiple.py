import requests
from bs4 import BeautifulSoup

base_url = 'https://scrapeme.live/shop/'
page_number = 1
products = []

while True:
    url = f'{base_url}?page={page_number}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    product_elements = soup.find_all('div', class_='content-area')
    
    if not product_elements:
        break

    for product in product_elements:
        product_name = product.find('h2', class_='woocommerce-loop-product__title').text.strip()
        product_price = product.find('span', class_='price').text.strip()
        products.append((product_name, product_price))
    
    page_number += 1
    if page_number > 4:
        break

for product_name, product_price in products:
    print(f"Product: {product_name}, Price: {product_price}")


