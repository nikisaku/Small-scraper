from get_data import get_data
from get_tags import get_tags
from all_pages import all_pages
from check_dir import check_dir
from save_to import save_to
from write_posts import write_posts
from write_tags import write_tags
from get_external_links import get_external_links
from get_title_from_external_page import get_title

SUBPAGE_START = 1
SUBPAGE_END = 56
notes_dir = '_notes'
check_dir = check_dir(notes_dir)
save_path = save_to(notes_dir)
pages = range(SUBPAGE_START, SUBPAGE_END)

for url in all_pages(pages):
    content = get_data(url)
    follow = get_external_links(content.get('link'))
    title = get_title(follow)
    write_posts(content, url, save_path, title)

for url in all_pages(pages):
    all_tags = get_tags(url)
    for tag in all_tags:
        write_tags(tag, save_path)
