# this function download all tass html pages for future work

import requests
from tools.create_sub_directory import create_directory

cookies = {
    'PHPSESSID': 'e2dqn3gijb6c6ri382r4vu8ob5',
    'uiPrefs': 'a%3A4%3A%7Bs%3A21%3A%22isBottomLightboxShown%22%3Bb%3A0%3Bs%3A23%3A%22isLayoutLeftColumnShown%22%3Bb%3A1%3Bs%3A24%3A%22isLayoutRightColumnShown%22%3Bb%3A0%3Bs%3A50%3A%22pagination_asset_fullTextSearch_nb_thumbs_per_page%22%3Bs%3A3%3A%22200%22%3B%7D',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/117.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en,en-US;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',
    'Connection': 'keep-alive',
    # 'Cookie': 'PHPSESSID=e2dqn3gijb6c6ri382r4vu8ob5; uiPrefs=a%3A4%3A%7Bs%3A21%3A%22isBottomLightboxShown%22%3Bb%3A0%3Bs%3A23%3A%22isLayoutLeftColumnShown%22%3Bb%3A1%3Bs%3A24%3A%22isLayoutRightColumnShown%22%3Bb%3A0%3Bs%3A50%3A%22pagination_asset_fullTextSearch_nb_thumbs_per_page%22%3Bs%3A3%3A%22200%22%3B%7D',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}




def get_response(url):
    response = requests.get(
        url=url,
        cookies=cookies,
        headers=headers,
    )
    return response

def save_responce_as_html(url):
    response = get_response(url)

    with open(f"tass_html/rezult_tass_{url.split('/')[-1]}.html", 'w') as html_file:
        html_file.write(response.text)

def page_pagination(page_number):
    url = f'https://www.tassphoto.com/ru/asset/fullTextSearch/search/%D0%A1%D0%B5%D0%BC%D0%B5%D0%BD+%D0%9B%D0%B8%D1%85%D0%BE%D0%B4%D0%B5%D0%B5%D0%B2/page/{page_number}'
    save_responce_as_html(url)

if __name__ == '__main__':
    create_directory(".", 'tass_html')
    for i in range(21):
        page_pagination(i + 1)