#!/usr/bin/python3
import urllib.request
import sys


url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    head_id = response.getheader('X-Request-Id')
    print(head_id)
