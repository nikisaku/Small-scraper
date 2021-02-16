import requests
from bs4 import BeautifulSoup
import re
import os
from pathlib import Path
from get_data import get_data
from get_tags import get_tags
import unidecode

# setting up saving path for future files
workspace = Path(os.getcwd())
saveto = Path(workspace, '_notes')

# if dir _notes doesn't exist, it'll be created
if os.path.isdir(saveto):
    pass
else:
    saveto.mkdir()

# range for subpages
pages = range(1, 2)

# list for post urls
urls = []

# going through every subpage
for page in pages:
    page = requests.get('https://doomhammersupposeserroneously.tumblr.com/page/' + str(page)).text
    soup = BeautifulSoup(page, 'html.parser')

    # grabbing all post <a> tagged
    post = soup.find_all("a", attrs={"href": re.compile('^https://doomhammersupposeserroneously.tumblr.com/post/')})

    # stripping <a> tagged from garbage and appending pure post links to the urls list
    for link in post:
        url = link.get('href')

        urls.append(url)

# going through every url in urls list to grab tagged and iframe
for url in urls:
    content = get_data(url)

    # writing every note to a separate file with unique name, based on post url from tumblr
    for entry in content:
        note_file_name = url.split('/')[4] + '.md'
        with open(saveto/note_file_name, 'w', encoding='utf-8') as f:
            f.write(f"---\n"
                    f"title: '{re.sub('[^0-9]', '', f.name)}'\n"
                    f"---\n")
            for key, value in content.items():
                if type(value) is list:
                    f.write(f"{key}: [[{']], [['.join(value)}]]")
                else:
                    f.write(f"\n{value}")
                    f.close()

# grabbing evey tag from every note and writing it a separate .md file
for url in urls:
    all_tags = get_tags(url)
    for tag in all_tags:
        tag_file_name = tag + '.md'
        with open(saveto/unidecode.unidecode(tag_file_name), 'w', encoding='utf-8') as f:
            f.write('---\n'
                    'layout: note\n'
                    f'title: {tag}\n'
                    '---')
            f.close()
