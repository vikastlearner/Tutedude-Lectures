import requests
from bs4 import BeautifulSoup
import csv

def Extract(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
    }
    response = requests.get(url=url, headers = headers).content

    # print(response.content)
    soup = BeautifulSoup(response, 'lxml') # second one is parser - html, lxml
    tag = soup.find("div", {"id": "mp-right"}) # name of the tag
    # print(tag)
    # h = tag.find("h2", {"id":"mp-itn-h2"})
    h = tag.find_all("h2") # prints all h2 data under "div (tag)"
    # h = tag.find("h2", {"id":"mp-itn-h2"}).find(...) # prints selected find data inside the h2.
    # print(h)
    content = [span.text for span in h]
    # print(content) # prints only the header.

    with open('wiki.csv', 'w') as f: # creates a file
        csv_writer = csv.writer(f) # Enables the file
        csv_writer.writerow(content)




Extract(url = 'https://en.wikipedia.org/wiki/Main_Page')