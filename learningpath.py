import requests
from bs4 import BeautifulSoup
import re
import csv


page = requests.get('https://doomhammersupposeserroneously.tumblr.com/post/190233642834').text
soup = BeautifulSoup(page, 'html.parser')

tags = []
yt_iframe = []
yt_secondary = []

div = soup.find_all('div', attrs={'class': 'tags'})
for entry in div:
    tags.append(entry.text)
    print(tags)

songs_links = soup.find_all('iframe')[0]
yt_iframe.append(songs_links)

print(yt_iframe)

yt = soup.find('meta', attrs={'name': 'twitter:player'})
yt_secondary.append(yt['content'])
print(yt_secondary)



# print(tags)
#
# with open('test.txt', 'w') as f:
#     for i in div:
#         f.write(str(i.text.strip()))
#         f.close()
