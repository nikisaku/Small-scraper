import unidecode


def write_posts(content, url, save_path, title):
    note_file_name = url.split('/')[4] + '.md'
    date = content.get('date')
    iframe = content.get('iframe')
    note_title = str(title).replace('[', '').replace(']', '')\
        .replace('\'', '').replace('\\', '').replace('+', 'with ')\
        .replace(':', '').replace('\"', '').replace('||', '|').replace(')', '').replace('(', '')

    with open(save_path/unidecode.unidecode(note_file_name), 'w', encoding='utf-8') as f:
        f.write(f"---\n"
                f"title: '{note_title}'\n"
                f"date: {date}\n"
                f"last_modified_at: {date}\n"
                f"---\n")
        for key, value in content.items():
            if type(value) is list:
                f.write(f"{key}: [[{']], [['.join(value)}]]")
            else:
                f.write(f"\n{iframe}")
                break
        f.close()
        print(note_file_name)
