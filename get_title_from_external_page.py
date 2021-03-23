import requests
from bs4 import BeautifulSoup
import random


def get_title(url):
    if url != None:
        page = requests.get(url).text
        soup = BeautifulSoup(page, 'html.parser')

        decoded_title = []
        title = soup.find('title')
        decoded_title.append(title.string)

        return decoded_title

    else:
        return 'Text or empty note'


if __name__ == '__main__':
    print(get_title('https://www.youtube.com/watch?v=g_QHytUuaMY'))
