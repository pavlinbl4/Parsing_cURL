import requests



from tools.create_sub_directory import create_directory
from tools.image_name_with_sales_count import add_sales_count_to_image_name
from tools.origanal_file_name import extract_image_name


def download_jpeg_image(image_link, sales_count):
    # create folder for images in root
    image_folder = create_directory("..", 'Images')

    # original file name from site
    image_name = extract_image_name(image_link)

    # add information about sales to file -  optional
    image_name_sales = add_sales_count_to_image_name(image_name, sales_count)

    try:
        r = requests.get(image_link, stream=True)
        with open(
                f'{image_folder}/{image_name_sales}',
                "bw") as f:
            for chunk in r.iter_content(9000):
                f.write(chunk)
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    download_jpeg_image("https://iv.kommersant.ru/relay/relayimage/1653806tyucolon20230929154700/200", 888)
