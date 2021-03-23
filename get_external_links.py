import requests
from bs4 import BeautifulSoup


def get_external_links(url):
    if url != None:
        page = requests.get(url).text
        soup = BeautifulSoup(page, 'html.parser')

        for link in soup.find_all('a', href=True):
            external_link = link.get('href')

            if external_link != '#':
                return external_link


if __name__ == "__main__":
    print(get_external_links(
        'https://www.youtube.com/embed/g_QHytUuaMY?feature=oembed&amp;enablejsapi=1&amp;origin=https://safe.txmblr.com&amp;wmode=opaque'))
