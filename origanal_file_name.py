import requests

url = "https://iv.kommersant.ru/relay/relayimage/1653806tyucolon20230929154700/200"


def extract_image_name(url):
    response = requests.get(url)

    if response.status_code == 200:
        if 'Content-Disposition' in response.headers:
            # Extracting the filename from the Content-Disposition header
            filename = response.headers['Content-Disposition'].split('filename=')[1].strip('"')

    return filename


assert extract_image_name("https://iv.kommersant.ru/relay/relayimage/1653806tyucolon20230929154700/200") == 'KSP_017764_00713_1.jpg'
