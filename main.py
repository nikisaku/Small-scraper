import requests
from bs4 import BeautifulSoup
import re
from get_data import get_data

# range for subpages
pages = range(1, 2)

# list for post urls
urls = []

# going through every subpage
for page in pages:
    page = requests.get('https://doomhammersupposeserroneously.tumblr.com/page/' + str(page)).text
    soup = BeautifulSoup(page, 'html.parser')

    # grabbing all post <a> tags
    post = soup.find_all("a", attrs={"href": re.compile('^https://doomhammersupposeserroneously.tumblr.com/post/')})

    # stripping <a> tags from garbage and appending pure post links to the urls list
    for link in post:
        url = link.get('href')

        urls.append(url)

for url in urls:
    content = get_data(url)

    with open('yada' + '.md', 'w', encoding='utf-8') as f:
        for key, value in content.items():
            if type(value) is list:
                f.write(f"---\n"
                        f"title: {f.name.strip('.md')}\n"
                        f"{key}: {', '.join(value)}")
            else:
                f.write(f"\n---\n{value}")
                f.close()
