import requests
from bs4 import BeautifulSoup


def get_data(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')

    # tags = []
    yt_iframe = []
    yt_secondary = []

    div = soup.find_all('div', attrs={'class': 'tags'})
    for entry in div:
        tags = entry.text.strip().replace('#', '').split('\n')

    # print(f"Tagi: {tags}")

    songs_links = soup.find_all('iframe')[0]
    yt_iframe.append(songs_links)

    # print(f"Link YT z kodem html: {yt_iframe}")

    yt = soup.find('meta', attrs={'name': 'twitter:player'})
    if yt is not None and 'content' in yt:
        yt_secondary.append(yt['content'])
    # print(f"Czysty link do samej piosenki: {yt_secondary}")

    entry = {'tags': tags,
             'yt if': yt_iframe,
             'yt sec': yt_secondary}
    return entry


if __name__ == "__main__":
    print(get_data('https://doomhammersupposeserroneously.tumblr.com/post/190233642834'))
