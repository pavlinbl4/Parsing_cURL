import os
from icecream import ic


def find_files(dir_path: str, extension: str) -> list:  # find all files with extension in directory
    return [f for f in os.listdir(dir_path) if f.endswith(extension)]


def file_name_and_dir_path(full_path: str):
    # Splitting the string on slash and joining back
    dir_path = '/'.join(full_path.split('/')[:-1])
    file_name = full_path.split('/')[-1]
    return file_name, dir_path


if __name__ == '__main__':
    ic(find_files('../kommersant', 'html'))
    # ic(find_files('../tass_html', 'html'))
