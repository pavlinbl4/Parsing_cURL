# this function download all tass html pages for future work

import requests

from delete_html_folder import delete_folder
from parse_tass_offline import main_check_downloaded_files, get_data, number_of_pages
from tools.create_sub_directory import create_directory
from tqdm import tqdm

from tass_curl import cookies, headers



def get_response(url):
    response = requests.get(
        url=url,
        cookies=cookies,
        headers=headers,
    )
    return response


def save_responce_as_html(url):
    response = get_response(url)

    total_size = int(response.headers.get('content-length', 0))
    block_size = 64  # 1 Kibibyte
    progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)

    for data in response.iter_content(block_size):
        progress_bar.update(len(data))

    progress_bar.close()

    with open(f"tass_html/rezult_tass_{url.split('/')[-1]}.html", 'w') as html_file:
        html_file.write(response.text)


def page_pagination(page_number):
    url = f'https://www.tassphoto.com/ru/asset/fullTextSearch/search/%D0%A1%D0%B5%D0%BC%D0%B5%D0%BD+%D0%9B%D0%B8%D1%85%D0%BE%D0%B4%D0%B5%D0%B5%D0%B2/page/{page_number}'
    save_responce_as_html(url)


def find_pages_number():
    #  how many pages I want to save

    # save first page
    page_pagination(1)

    # get amount of pages from first html file
    return number_of_pages(f'tass_html/rezult_tass_1.html')


def main():
    create_directory(".", 'tass_html')
    pages_count = int(find_pages_number())

    #  start to save pages from number 2
    for i in range(1, pages_count + 1):
        page_pagination(i + 1)
    main_check_downloaded_files()
    delete_folder('tass_html')


if __name__ == '__main__':
    main()


