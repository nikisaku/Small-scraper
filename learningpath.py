import requests
from bs4 import BeautifulSoup
import re
import csv


page = requests.get('https://doomhammersupposeserroneously.tumblr.com/post/190233642834').text
soup = BeautifulSoup(page, 'html.parser')

tags = []
yt_links = []

div = soup.find_all('div', attrs={'class': 'tags'})
for i in div:
    tags.append(i.text.strip())

print(tags)

div = soup.find_all('div', attrs={'class': 'tags'})
for i in div:
    tags.append(i.text.strip())
