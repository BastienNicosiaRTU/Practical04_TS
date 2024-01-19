import requests

# Basic GET request
GETresponse = requests.get('https://example.com')
print("\n Get \n")
print(GETresponse.text)

# GET request with parameters
params = {'key1': 'value1', 'key2': 'value2'}
Param_response = requests.get('https://example.com', params=params)
print("GetParam\n")
print(Param_response.url)

# POST request with form data
payload = {'key1': 'value1', 'key2': 'value2'}
Post_response = requests.post('https://httpbin.org/post', data=payload)
print("Post\n")
print(Post_response.text)

# POST request with multipart/form-data (for file uploads)
files = {'file': open('report.txt', 'rb')}
File_response = requests.post('https://httpbin.org/post', files=files)
print("Files\n")
print(File_response.text)
