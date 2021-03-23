import requests
from bs4 import BeautifulSoup


def get_tags(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')

    # scraping for tagged without hashtags, pure text
    div = soup.find_all('div', attrs={'class': 'tags'})
    for entry in div:
        tagged = entry.text.strip().replace('#', '').split('\n')
        return tagged


if __name__ == '__main__':
    print(get_tags('https://doomhammersupposeserroneously.tumblr.com/post/190139084820'))
