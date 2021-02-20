import re
import unidecode
from get_data import get_data
from get_tags import get_tags
from all_pages import all_pages
from check_dir import check_dir
from save_to import save_to
from write_posts import write_posts

notes_dir = '_notes'
check_if_theres_dir = check_dir(notes_dir)
save_path = save_to(notes_dir)
pages = range(1, 2)

for url in all_pages(pages):
    shite = get_data(url)
write_posts(shite, url, save_path)

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
