import os


def check_dir(dir_name):

    if os.path.isdir(dir_name):
        pass
    else:
        dir_name.mkdir()


if __name__ == '__main__':
    print(check_dir('_notes'))