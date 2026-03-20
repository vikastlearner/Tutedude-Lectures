import requests
url = 'http://127.0.0.1:8000/post/'
payload = {
    "title": "Post Webscrapper",
    "content": "This ie posted from Web scrapper"
}
response = requests.post(url = url, data = payload, auth = ("admin", "vikas1"))
print(response.text) # This shows the response after we posted, that is what is sent