import requests
api_url = 'https://jsonplaceholder.typicode.com/todos/909'

response = requests.get(api_url)
print(response.json())
print(response.status_code)

