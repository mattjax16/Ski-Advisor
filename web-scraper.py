'''
web-scraper.py
Author: Matt Bass

This is a web scraper to retrieve data on skis, and it puts that data in the ski database
'''

from bs4 import BeautifulSoup
import requests
from concurrent.futures import ThreadPoolExecutor


def loadWebPage(url: str) -> BeautifulSoup:
    page = requests.get(url)
    soup = BeautifulSoup(page)
    return soup


# Main function to run the web scraper
def main():

    url = 'https://soothski.com/compare/'

    soup = loadWebPage(url)

    print(soup.prettify())


main()
