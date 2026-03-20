import requests

# url = 'http://127.0.0.1:8000/app/app'
# print(dir(requests)) # TO get all the details

# for image downloading:
url = 'http://127.0.0.1:8000/static/blogs/images/python.png' # URL of image and not page.

user = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
}

response = requests.get(url=url, headers=user)
# print(response.request.headers) # This gives headers details

# to download image:
pic = response.content
f = open("python.png", "wb")
f.write(pic)

