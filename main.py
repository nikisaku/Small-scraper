import requests
from bs4 import BeautifulSoup
import re
import csv


# range for subpages
pages = range(1, 56)

# list for post urls
urls = []

# going through every subpage
for page in pages:
    page = requests.get("https://doomhammersupposeserroneously.tumblr.com/page/" + str(page)).text
    soup = BeautifulSoup(page, "html.parser")

    # grabbing all post <a> tags
    post = soup.find_all("a", attrs={"href": re.compile("^https://doomhammersupposeserroneously.tumblr.com/post/")})

    # stripping <a> tags from garbage and appending pure post links to the urls list
    for link in post:
        url = link.get('href')

        urls.append(url)
