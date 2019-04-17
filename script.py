
from urllib.request import urlopen, Request
from urllib.parse import urlencode, quote_plus
import time
import csv
import json

links = []
with open('site.csv', 'wb') as spreadsheet:
    writer = csv.writer(spreadsheet)
    file = open('sitemap.xml')
    file.readline();

    for line in file:
        link = line[10:-13]
        links.append(link)
        print(link)

    links[-1] = links[-1][:-8]
    print(links[-1])

    api_key = 'AIzaSyCZcMS8DoTtOP6Nvu_6C3T9pkpHhCs5oeI'

    service_url = "https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run"

    for link in links:
        request_url = link
        params = {
            'url': request_url,
            'key': api_key,
        }
        data = urlencode(params, quote_plus)
        data = data.encode('utf-8')
        req = Request(service_url, data)
        content = urlopen(req).read()
        print(content)
        time.sleep(2)
