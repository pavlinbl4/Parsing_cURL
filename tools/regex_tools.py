import re
from icecream import ic


def images_number_int(text_line: str, pattern) -> int:
    return int(re.search(pattern, text_line).group())


def extract_extension(file_name: str) -> str:
    # return re.search(r"\.(\w+)$", file_name)
    return re.search(r"\.\w+\Z", file_name).group()


def file_name_no_extension(file_name: str) -> str:
    # return re.search(r".+\.", file_name).group()
    return re.search(r"^(?:.*\/)?([^\/]+?|)(?=(?:\.[^\/.]*)?$)", file_name).group()


if __name__ == '__main__':
    assert images_number_int('Ваши фото (позиций: 29335)', pattern=r'(?<=позиций:\s)\d+') == 29335
    assert images_number_int('продаж: 1', pattern=r'(?<=продаж:\s)\d+') == 1
    # assert file_name_no_extension('example.file.name') == 'example.file'
    print(file_name_no_extension('example.file.name'))
    print(extract_extension('file.name_with.dots.extensio1'))
