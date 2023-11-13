from tools.image_downloader import download_jpeg_image
from tools.files_work import find_files
from tools.origanal_file_name import extract_image_name
from tools.regex_tools import images_number_int
from tools.soup import make_soup_from_offline_file
from tqdm import tqdm

from tools.u_xlsx_writer import universal_xlsx_writer


def get_kommersant_data(offline_html, count: int) -> int:
    soup = make_soup_from_offline_file(offline_html)
    all_thumbs_data = soup.find_all('div', class_='ps_mosaic__items')
    thumb_data = all_thumbs_data[0].find_all('div', class_="ps_mosaic__item")
    sales_on_one_file = 0
    for image in thumb_data:
        sales_number = image.find(class_="ps_sales ps_sales--green").text
        sales_number_int = images_number_int(sales_number, pattern=r'(?<=продаж:\s)\d+')
        if sales_number_int != 0:
            sales_on_one_file += sales_number_int
            # count += sales_number_int
            # print(sales_number)
            # print(image.find(class_="ps_mosaic__item_text").text)
            image_link = image.find('img', class_="ps_lenta__image").get('src')
            # download_jpeg_image(image_link, sales_number_int)
            universal_xlsx_writer(['Sales', 'Image id'],
                                  '/Volumes/big4photo/Documents/Kommersant/external_sales.xlsx',
                                  "external_sales",
                                  photographer=None, row_line=None,
                                  column_number=None,
                                  cell_data=None,
                                  row_data=[str(sales_number_int), extract_image_name(image_link)], column_width=30)
    count += sales_on_one_file
    return count


def main_check_downloaded_files(dir_path: str):
    all_html_files = find_files(dir_path, 'html')
    count = 0
    for number, file in tqdm(enumerate(all_html_files, start=1)):
        count = get_kommersant_data(f'{dir_path}/rezult_{number}.html', count)
    print(f'Sales on all pages{count = }')


if __name__ == '__main__':
    main_check_downloaded_files('./kommersant')
    # get_kommersant_data('./kommersant/rezult_2.html', 0)
