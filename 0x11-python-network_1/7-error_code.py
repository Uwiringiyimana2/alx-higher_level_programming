#!/usr/bin/python3
import requests
import sys


url = sys.argv[1]
r = requests.get(url)

try:
    print(r.text)
except HTTPError as e:
    if r.status_code >= 400:
        print("Error code:", e.reason)
