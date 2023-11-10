from tools.files_work import find_files
from tools.regex_tools import images_number_int
from tools.soup import make_soup_from_offline_file
from icecream import ic


def get_kommersant_data(offline_html):
    soup = make_soup_from_offline_file(offline_html)

    #  table with all images  -  class="ps_mosaic__items"
    all_thumbs_data = soup.find_all('div', class_='ps_mosaic__items')

    thumb_data = all_thumbs_data[0].find_all('div', class_="ps_mosaic__item")

    for image in thumb_data:
        sales_number = image.find(class_="ps_sales ps_sales--green").text
        if images_number_int(sales_number, pattern=r'(?<=продаж:\s)\d+') != 0:
            print(sales_number)
            print(image.find(class_="ps_mosaic__item_text").text)
            print(image.find('img', class_="ps_lenta__image").get('src'))


def main_check_downloaded_files(dir_path: str):
    ic(dir_path)
    all_html_files = find_files(dir_path, 'html')
    for number, file in enumerate(all_html_files):
        print(f'{number} rezult_{number + 1}.html\n{"*" * 200}')
        get_kommersant_data(f'{dir_path}/{file}')


if __name__ == '__main__':
    main_check_downloaded_files('./kommersant')
    # get_kommersant_data('./kommersant/rezult_2.html')
