from get_data import get_data
from get_tags import get_tags
from all_pages import all_pages
from check_dir import check_dir
from save_to import save_to
from write_posts import write_posts
from write_tags import write_tags

SUBPAGE_START = 1
SUBPAGE_END = 56
notes_dir = '_notes'
check_dir = check_dir(notes_dir)
save_path = save_to(notes_dir)
pages = range(SUBPAGE_START, SUBPAGE_END)

for url in all_pages(pages):
    content = get_data(url)
    write_posts(content, url, save_path)

for url in all_pages(pages):
    all_tags = get_tags(url)
    for tag in all_tags:
        write_tags(tag, save_path)
