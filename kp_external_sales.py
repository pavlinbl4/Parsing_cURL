from check_cycle_limit import calculate_limit
from tools.create_sub_directory import create_directory
import requests
from ksp_curl_old import cookies, headers, params
from tqdm import tqdm, trange


def kp_pagination():
    html_files_dir = create_directory(".", 'kommersant')

    # get number of pages in site
    pages_count = calculate_limit(int(params['total']))

    print(f"Now {params['total']} images  on site,\n{pages_count} pages would be downloaded")

    for i in trange(1, pages_count + 1):
        params['pageprms.pagenum'] = i

        response = requests.get('https://photo.kommersant.ru/photo/user_photo_download', params=params,
                                cookies=cookies,
                                headers=headers)

        with open(f"{html_files_dir}/rezult_{i}.html", 'w') as html_file:
            html_file.write(response.text)


if __name__ == '__main__':
    kp_pagination()
