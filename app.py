import time

import requests
from bs4 import BeautifulSoup

from config import *


def make_request(url, method="GET", payload=None):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0 Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0."}

    if method == "GET":
        r = requests.get(url, headers=headers)
    elif method == "POST":
        r = requests.post(url, headers=headers, data=payload)
    if r.status_code == 200:
        if method == "POST":
            print(r.text)
        return r
    else:
        print(r.status_code, url)

class DaftScraper(object):

    def __init__(self):
        self.property_list = []
        self.populate()
        self.monitor()

    def populate(self):
        """
        Populates the program memory with properties on start of the program to compare on the next run
        """
        print('Adding current properties to program memory')
        property_urls = self.get_properties_urls()
        [self.property_list.append(url) for url in property_urls]
        
    def monitor(self):
        """
        Visit the url every few seconds to check if new properties were added
        """
        while True:
            print('Checking for new properties')
            self.check_for_new_properties()
            time.sleep(INTERVAL)

    def check_for_new_properties(self):
        """
        Checks if new property url appeared in the results, and sends post request if yes
        """
        property_urls = self.get_properties_urls()

        for url in property_urls:
            if url not in self.property_list:
                print('Found new property...messaging', url)
                self.message_property(url)
                self.property_list.append(url)
        

    @staticmethod
    def get_properties_urls():
        """
        Gathers latest properties urls to check
        :return: list of urls
        """
        r = make_request(LINK_TO_MONITOR)
        soup = BeautifulSoup(r.content, 'html.parser')
        property_boxes = soup.find_all('div', {'class': 'box'})
        return ['https://www.daft.ie' + x.find('a')['href'] for x in property_boxes]


if __name__ == "__main__":
    DaftScraper()
