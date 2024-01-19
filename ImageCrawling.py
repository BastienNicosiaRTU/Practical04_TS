import requests
from bs4 import BeautifulSoup
import os

# URL of the webpage with images
url = 'https://www.freepng.fr/'

# Send a GET request to the webpage
response = requests.get(url)

# Parse the webpage content with Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all image tags
image_tags = soup.find_all('img')

# Directory to save images
os.makedirs('downloaded_images', exist_ok=True)

# Loop through image tags and download images
for img in image_tags:
    img_url = img.get('src')
    if img_url:
        # Complete the image URL if it's relative
        if img_url.startswith('/'):
            img_url = url + img_url

        # Extract image name from URL
        img_name = img_url.split('/')[-1]

        # Download and save the image
        img_response = requests.get(img_url)
        with open(f'downloaded_images/{img_name}', 'wb') as f:
            f.write(img_response.content)

print("Images downloaded successfully.")
