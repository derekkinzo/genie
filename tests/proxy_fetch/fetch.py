import csv
import pdb
import hashlib
import pdb
import random
import requests
import sys
import time
from bs4 import BeautifulSoup

def gen_cookie():
    gid = hashlib.md5(str(random.random()).encode('utf-8')).hexdigest()[:16]
    return {'GSP': 'ID={0}:CF=4'.format(gid)}

_HEADERS = {
    'accept-language': 'en-US,en',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/41.0.2272.76 Chrome/41.0.2272.76 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml'
    }
_HOST = 'https://scholar.google.com'
_SESSION = requests.Session()
_PAGESIZE = 5

def get_proxy(addr):
    return {
        "http": "http://" + addr,
        "https": "https://" + addr
    }

titles = []
with open("articles.csv", "r") as results_file:
    reader = csv.reader(results_file)
    next(reader)
    for row in reader:
        titles.append(row[1])
random.shuffle(titles)

proxies = []
with open("proxies.csv", "r") as results_file:
    reader = csv.reader(results_file)
    next(reader)
    for row in reader:
        proxies.append(row[0])
random.shuffle(proxies)
current_proxy = 0
ttt = time.time()
for i in range(len(titles)):
    url = f"{_HOST}/scholar?q={requests.utils.quote(titles[i])}"
    response = requests.get(url, headers=_HEADERS, cookies=gen_cookie())
    text = response.text
    text.replace(u'\xa0', u' ')
    bs = BeautifulSoup(text, 'html.parser')
    print(f"processed {i} at time = {time.time() - ttt}")
    if bs.find(class_='gs_ico gs_ico_nav_next'):
        print(bs.find(class_='gs_ico gs_ico_nav_next').parent['href'])
