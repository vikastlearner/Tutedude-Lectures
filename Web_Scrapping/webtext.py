# This will give us the output in string
# Basically it will have coding of the file.

import requests
url = 'http://127.0.0.1:8000/allposts'

response = requests.get(url= url)
# print(response.text)
# print(response) # This gives response code
# print(response.status_code) # This gives response's status code
