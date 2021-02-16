import requests
from bs4 import BeautifulSoup


def get_data(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')

    # lists for iframe HTML and tags
    iframe = []

    # scraping for tagged without hashtags, pure text
    div = soup.find_all('div', attrs={'class': 'tags'})
    for entry in div:
        tags = entry.text.strip().replace('#', '').split('\n')

    # scraping for iframe HTML tagged and appending them to the iframe list
    songs_links = soup.find_all('iframe')[0]
    iframe.append(songs_links)

    # making a dictionary out of tagged and iframe
    entry = {'tagged': tags,
             'iframe': songs_links}
    return entry


if __name__ == "__main__":
    print(get_data('https://doomhammersupposeserroneously.tumblr.com/post/190233642834'))
