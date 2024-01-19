import requests

# Basic GET request
GET_response = requests.get('https://example.com')
print("\n Get \n")
print(GET_response.text)

# GET request with parameters
params = {'key1': 'value1', 'key2': 'value2'}
Get_response_param = requests.get('https://example.com', params=params)
print("GetParam\n")
print(Get_response_param.url)

# POST request with form data
payload = {'key1': 'value1', 'key2': 'value2'}
Post_response_Form = requests.post('https://httpbin.org/post', data=payload)
print("Post\n")
print(Post_response_Form.text)

# POST request with multipart/form-data (for file uploads)
files = {'file': open('report.txt', 'rb')}
Post_response_file = requests.post('https://httpbin.org/post', files=files)
print("Files\n")
print(Post_response_file.text)
 
 #PUT requests.
payload = {'key1': 'newvalue'}
PUT_response = requests.put('https://httpbin.org/put', data=payload)
print("Put\n")
print(PUT_response.text)

#Delete requests.
Del_response = requests.delete('https://httpbin.org/delete')
print("Del\n")
print(Del_response.text)

#Head request
Head_response= requests.head('https://example.com')
print("Head\n")
print(Head_response.headers)

#Path request
payload = {'key1': 'updatedvalue'}
Path_response = requests.patch('https://httpbin.org/patch', data=payload)
print("Paht\n")
print(Path_response.text)

#Option Request
Option_response = requests.options('https://httpbin.org')
print("Option\n")
print(Option_response.headers)





