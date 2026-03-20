import requests
from bs4 import BeautifulSoup
import re

image = input("Enter the image name: ")

user_agent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0"
    }
# url = f"https://www.google.com/search?q={image}&sca_esv=ea5941a1fd0faf3f&sxsrf=ANbL-n4wd_t9kyWzivEfCdQDu7wVoCzedg:1774002705996&source=hp&biw=1678&bih=1105&ei=ESK9ab2VOvHL1e8P9-6aoAw&iflsig=AFdpzrgAAAAAab0wITUnutsSylHWKbXjdZ2-2-sA3Snn&ved=0ahUKEwj94fmIo66TAxXxZfUHHXe3BsQQ4dUDCBc&uact=5&oq=moon&gs_lp=EgNpbWciBG1vb24yDhAAGIAEGLEDGIMBGIoFMgsQABiABBixAxiDATIIEAAYgAQYsQMyDhAAGIAEGLEDGIMBGIoFMg4QABiABBixAxiDARiKBTIIEAAYgAQYsQMyCxAAGIAEGLEDGIMBMgsQABiABBixAxiDATIFEAAYgAQyCBAAGIAEGLEDSJsRUJwLWKAPcAF4AJABAJgBoQGgAZ0EqgEDMC40uAEDyAEA-AEBigILZ3dzLXdpei1pbWeYAgWgArIEqAIKwgIKECMYJxjJAhjqAsICBxAjGCcYyQKYAweSBwMxLjSgB4kUsgcDMC40uAeqBMIHBTAuMy4yyAcOgAgA&sclient=img&udm=2"
url = f"https://www.bing.com/images/search?q={image}+image&qpvt=moon+image&form=IQFRML&first=1&cw=2537&ch=1308"
response = requests.get(url = url, headers=user_agent).text
soup = BeautifulSoup(response, "lxml")
# print("https" in response) # to pint the content of image web page.
#print(response)
images = soup.find_all('img')
for img in images:
    print(img.get("jpg"))

# To find only the link of the images:
# pattern = ""
# images = re.findall(, response)
# for image in images:
#     print(image)

