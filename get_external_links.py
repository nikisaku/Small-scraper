import requests
from bs4 import BeautifulSoup


def get_external_links(url):
    if url is not None:
        page = requests.get(url).text
        soup = BeautifulSoup(page, 'html.parser')

        for link in soup.find_all('link', rel="canonical", href=True):
            external_link = link.get('href')
            return external_link

        for bandcamp_link in soup.find_all('a', href=True):
            bandcamp = bandcamp_link.get('href')
            if bandcamp != '#':
                return bandcamp


if __name__ == "__main__":
    print(get_external_links(
        'https://w.soundcloud.com/player/?url=https%3A%2F%2Fapi.soundcloud.com%2Ftracks%2F75234063&amp;visual=true&amp;liking=false&amp;sharing=false&amp;auto_play=false&amp;show_comments=false&amp;continuous_play=false&amp;origin=tumblr'))
