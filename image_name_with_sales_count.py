from tools.regex_tools import file_name_no_extension, extract_extension


def add_sales_count_to_image_name(image_name: str, sales_count):
    return f'{file_name_no_extension(image_name)}__{str(sales_count)}{extract_extension(image_name)}'


if __name__ == '__main__':
    assert (add_sales_count_to_image_name('example.file.name', 99)) == 'example.file__99.name'
