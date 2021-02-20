
import re
import os
from pathlib import Path
import unidecode
from get_data import get_data
from get_tags import get_tags
from all_pages import all_pages
from check_dir import check_dir
from save_to import save_to

notes = check_dir('_notes')
save_path = save_to('_notes')
pages = range(1, 2)
# going through every url in urls list to grab tagged and iframe
for url in all_pages(pages):
    content = get_data(url)

    # writing every note to a separate file with unique name, based on post url from tumblr
    for entry in content:
        note_file_name = url.split('/')[4] + '.md'
        with open(save_path/note_file_name, 'w', encoding='utf-8') as f:
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
for url in all_pages(pages):
    all_tags = get_tags(url)
    for tag in all_tags:
        tag_file_name = tag + '.md'
        with open(save_path/unidecode.unidecode(tag_file_name.replace(':', '-').replace(' ', '-').replace('  ', '-')),
                  'w', encoding='utf-8') as f:
            f.write('---\n'
                    'layout: note\n'
                    f'title: "{tag}"\n'
                    '---')
            f.close()
