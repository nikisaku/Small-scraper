import requests
from bs4 import BeautifulSoup
import re


def all_pages(pages):

    urls = []

    for page in pages:
        page = requests.get('https://doomhammersupposeserroneously.tumblr.com/page/' + str(page)).text
        soup = BeautifulSoup(page, 'html.parser')

        # grabbing all post <a> tagged
        post = soup.find_all("a", attrs={"href": re.compile('^https://doomhammersupposeserroneously.tumblr.com/post/')})

        # stripping <a> tagged from garbage and appending pure post links to the urls list
        for link in post:
            url = link.get('href')

            urls.append(url)
    return urls


if __name__ == '__main__':
    print(all_pages(range(1, 3)))
