import requests

# Define the search engine URL and the search keyword
search_engine_url = "https://www.google.com/"
search_keyword = "Python Web Crawler"

# Parameters for the GET request
params = {'q': search_keyword}

# Send the GET request
response = requests.get(search_engine_url, params=params)

# Print the response text or URL
print(response.url)  # or print(response.url)
