
from urllib.request import urlopen, Request
from urllib.parse import urlencode, quote_plus
import time
import csv
import ast

links = []
with open('site.csv', 'w') as spreadsheet:
    writer = csv.writer(spreadsheet,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    file = open('sitemap.xml')
    file.readline();

    for line in file:
        link = line[10:-13]
        links.append(link)

    links[-1] = links[-1][:-8]

    api_key = 'AIzaSyCZcMS8DoTtOP6Nvu_6C3T9pkpHhCs5oeI'

    service_url = "https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run"

    writer.writerow(['url','is mobile friendly', 'errors'])
    for link in links:
        sheetLine = [link]
        time.sleep(5)
        request_url = link
        params = {
            'url': request_url,
            'key': api_key,
        }
        data = urlencode(params, quote_plus)
        data = data.encode('utf-8')
        req = Request(service_url, data)
        content = urlopen(req).read()
        content = ast.literal_eval(content.decode('utf-8'))

        if(content["mobileFriendliness"] == 'NOT_MOBILE_FRIENDLY'):
            sheetLine.append('N')
            errors = ""
            for error in content["mobileFriendlyIssues"]:
                errors += error['rule'] + " /"
            sheetLine.append(errors)
        else:
            sheetLine.append('Y')
        writer.writerow(sheetLine)
        print(content)
