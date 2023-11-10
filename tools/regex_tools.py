import re
from icecream import ic


def images_number_int(text_line: str, pattern) -> int:
    return int(re.search(pattern, text_line).group())


if __name__ == '__main__':
    assert images_number_int('Ваши фото (позиций: 29335)', pattern=r'(?<=позиций:\s)\d+') == 29335
    assert images_number_int('продаж: 1', pattern=r'(?<=продаж:\s)\d+') == 1
