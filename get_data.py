import requests
from bs4 import BeautifulSoup


def get_data(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')

    iframe = []
    yt_secondary = []

    div = soup.find_all('div', attrs={'class': 'tags'})
    for entry in div:
        tags = entry.text.strip().replace('#', '').split('\n')

    # print(f"Tagi: {tags}")

    songs_links = soup.find_all('iframe')[0]
    iframe.append(songs_links)

    # print(f"Link YT z kodem html: {iframe}")

    # yt = soup.find('meta', attrs={'name': 'twitter:player'})
    # if yt is not None:
    #     if 'content' in yt:
    #         yt_secondary.append(yt['content'])
    # print(f"Czysty link do samej piosenki: {yt_secondary}")

    entry = {'tags': tags,
             'iframe': songs_links}
    return entry


if __name__ == "__main__":
    raw_data = get_data('https://doomhammersupposeserroneously.tumblr.com/post/190233642834')

    with open("test.md", "w", ) as f:
        for key, value in raw_data.items():
            if type(value) is list:
                f.write(f"---\n"
                        f"title: {f.name.strip('.md')}\n"
                        f"{key}: {', '.join(value)}")
            else:
                f.write(f"\n---\n{value}")
                f.close()
