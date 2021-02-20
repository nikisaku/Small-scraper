import os
from pathlib import Path


def check_dir(dir_name):
    workspace = Path(os.getcwd())
    save_to = Path(workspace, dir_name)

    if os.path.isdir(dir_name):
        pass
    else:
        save_to.mkdir()


if __name__ == '__main__':
    print(check_dir('_notes'))
