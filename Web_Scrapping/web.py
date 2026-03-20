import urllib.request, urllib.parse, urllib.error

url = urllib.request.urlopen('http://127.0.0.1:8000/app/app')
for line in url:
    print(line.decode().strip())
    