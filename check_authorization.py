from tools.soup import make_soup_from_offline_file
from icecream import ic


def check_page(path_to_html: str)-> bool:
    soup = make_soup_from_offline_file(path_to_html)
    if soup.find('div', class_="ps_global_error") is None:
        return True
    return False


if __name__ == '__main__':
    assert check_page('tests/files for test/rezult_1.html') == True
    assert check_page('tests/files for test/_bad_authorization.html') == False

