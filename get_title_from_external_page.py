import requests
from bs4 import BeautifulSoup
from unidecode import unidecode


def get_title(url):
    if url is not None:
        page = requests.get(url).text
        soup = BeautifulSoup(page, 'html.parser')

        decoded_title = []
        title = soup.find('title')

        while title.string != "Zanim przejdziesz do YouTube":
            decoded_title.append(title.string)
            print(f"pass: {title.string.encode('utf8')}")
            break
        else:
            print(f"fail: {url}")
            title_2 = get_title(url)
            decoded_title.append(title_2)
            print(f"appended title: {title_2}")

        return decoded_title

    else:
        return 'Text or empty note'


if __name__ == '__main__':
    print(get_title('https://www.youtube.com/watch?v=dCpA7rJlEjU'))
