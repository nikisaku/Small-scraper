import unidecode


def write_tags(tag, save_path):
    tag_file_name = tag + '.md'
    with open(save_path/unidecode.unidecode(tag_file_name
                                                    .replace(' ', '-').replace(':', '-')
                                                    .replace('[', '').replace(']', '').replace(' ', '')),
              'w', encoding='utf-8') as f:
        f.write('---\n'
                'layout: note\n'
                f'title: "{tag}"\n'
                '---')
        f.close()
