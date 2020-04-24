import requests
import pdb
import csv
from lxml.html import fromstring
def get_proxies():
    url = "https://www.us-proxy.org/"
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr'):
        t = i.xpath('.//td[5]/text()')
        if t and t[0] == "elite proxy":
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)

    with open("proxies.csv", "w") as results_file:
        writer = csv.writer(results_file)
        for proxy in proxies:
            writer.writerow([proxy])


get_proxies()
