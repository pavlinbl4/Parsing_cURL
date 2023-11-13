# pip install lxml

from bs4 import BeautifulSoup

from tools.read_html import read_html


def get_soup(html):
    return BeautifulSoup(html, 'lxml')


def make_soup_from_offline_file(offline_html):
    offline_file = read_html(offline_html)
    soup = get_soup(offline_file)
    return soup


def get_html(link, browser):
    browser.get(link)
    html = browser.page_source
    return html
