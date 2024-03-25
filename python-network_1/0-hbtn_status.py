#!/usr/bin/python3
import urllib.request
""" Fetches from https://alu-intranet.hbtn.io/status"""

url = 'https://alu-intranet.hbtn.io/status'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    '\n    AppleWebKit/537.36 (KHTML, like Gecko)'
    '\n    Chrome/99.0.4844.84 Safari/537.36',
}

req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as response:
    content = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
    print("\t- utf8 content: {}".format(content.decode("utf-8")))
