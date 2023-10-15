from tools.clear_caption import clear_author
from tools.files_work import find_files
from tools.read_html import read_html
from tools.soup import get_soup
from u_xlsx_writer import universal_xlsx_writer
from datetime import datetime




def make_soup_from_offline_file(offline_html):
    offline_file = read_html(offline_html)
    soup = get_soup(offline_file)
    return soup


def thumbs_date_on_page(soup):
    thumbs_data = soup.find('ul', id="mosaic").find_all('div', class_="thumb-content thumb-width thumb-height")
    images_on_page = len(soup.find('ul', id="mosaic").find_all('a', class_="zoom"))
    return thumbs_data, images_on_page


def image_info(thumbs_data, images_on_page):
    for image_number_on_page in range(images_on_page):
        image_date = thumbs_data[image_number_on_page].find(class_="date").text
        image_id = thumbs_data[image_number_on_page].find(class_="title").text
        # image_title = thumbs_data[image_number_on_page].find('p').text
        image_caption = (thumbs_data[image_number_on_page].find('br')
                         .next_sibling.next_sibling.next_sibling.strip()
                         .replace(' Семен Лиходеев/ТАСС', '')).strip()
        image_pr_link = thumbs_data[image_number_on_page].find('img').get('src')

        image_caption = clear_author(image_caption)

        print(image_id, image_date, image_caption)
        # print(f'{image_pr_link = }')

        row_data = (image_id, image_date, image_caption, image_pr_link)

        today_date = f'{datetime.now().strftime("%d.%m.%Y")}'

        universal_xlsx_writer(row_data=row_data,
                              columns_names=('image_id',
                                             'image date',
                                             'image caption',
                                             'image link'),
                              file_path='/Volumes/big4photo/Documents/TASS/Tass_data/added_TASS_images.xlsx',
                              sheet_name=today_date,
                              column_width=(15, 15, 110, 50))


def get_data(offline_html):
    soup = make_soup_from_offline_file(offline_html)
    thumbs_data, images_on_page = thumbs_date_on_page(soup)
    image_info(thumbs_data, images_on_page)


if __name__ == '__main__':
    all_html_files = find_files('tass_html', 'html')

    for number, file in enumerate(all_html_files):
        print(f'Page - {number} - {"*"} * {200}')
        get_data(f'tass_html/{file}')
    # get_data(f'tass_html/rezult_tass_21.html')
