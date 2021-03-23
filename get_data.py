import requests
from bs4 import BeautifulSoup
import re


def get_data(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')

    # lists for iframe HTML and tags
    date_published = []

    for item in re.finditer('datePublished":"(.+?)"', page):
        date_published.append(item.group(1))
    date_split = str(date_published).split('T')
    date_decoded = str(date_split[0]).strip('[').replace("\'2", "2")

    # scraping for tagged without hashtags, pure text
    div = soup.find_all('div', attrs={'class': 'tags'})
    for entry in div:
        tags = entry.text.strip().replace('#', '').split('\n')

    # scraping for iframe HTML tagged and appending them to the iframe list
    songs_links = soup.find_all('iframe')[0]

    # getting pure link
    link = songs_links.get('src')

    # making a dictionary out of tagged and iframe
    entry = {'tagged': tags,
             'iframe': songs_links,
             'date': date_decoded,
             'link': link}

    return entry


if __name__ == "__main__":
    print(get_data('https://doomhammersupposeserroneously.tumblr.com/post/177055396469/kita-koguta-break-da-funk-kita-koguta'))
