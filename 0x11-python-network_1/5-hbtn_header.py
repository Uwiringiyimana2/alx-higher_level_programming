#!/usr/bin/python3
import requests
import sys


url = sys.argv[1]
r = requests.get(url)
print(r.headers['X-Request-Id'])
