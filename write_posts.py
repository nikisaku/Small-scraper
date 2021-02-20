import re


def write_posts(content, url, save_path):
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
