import requests
from bs4 import BeautifulSoup


def get_data(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')

    # tags = []
    iframe = []
    yt_secondary = []

    div = soup.find_all('div', attrs={'class': 'tags'})
    for entry in div:
        tags = entry.text.strip().replace('#', '').split('\n')

    # print(f"Tagi: {tags}")

    songs_links = soup.find_all('iframe')[0]
    iframe.append(songs_links)

    # print(f"Link YT z kodem html: {iframe}")

    yt = soup.find('meta', attrs={'name': 'twitter:player'})
    if yt is not None:
        if 'content' in yt:
            yt_secondary.append(yt['content'])
    # print(f"Czysty link do samej piosenki: {yt_secondary}")

    entry = {'tags': tags,
             'iframe': iframe,
             'yt sec': yt_secondary}
    return entry


if __name__ == "__main__":
    print(get_data('https://doomhammersupposeserroneously.tumblr.com/post/190233642834'))
    print(get_data('https://doomhammersupposeserroneously.tumblr.com/post/178079443346/01-eva-zaspany'))
    print(get_data('https://doomhammersupposeserroneously.tumblr.com/post/184057270392/buzzcocks-ever-fallen-in-love-with-someone-you'))
