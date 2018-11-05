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
