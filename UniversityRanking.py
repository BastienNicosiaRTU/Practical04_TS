import requests
from bs4 import BeautifulSoup
from lxml import html


url = 'https://www.shanghairanking.com/rankings/arwu/2023'
response = requests.get(url)
webpage_content = response.content

soup = BeautifulSoup(webpage_content, 'html.parser')

rankings = []
for row in soup.find_all('tr'):  
    columns = row.find_all('td')
    if columns:
        rank = columns[0].text.strip()
        university_name = columns[1].text.strip()
        rankings.append((rank, university_name))

tree = html.fromstring(webpage_content)


for rank, university in rankings:
    print(f"Rank: {rank}, University: {university} \n")
