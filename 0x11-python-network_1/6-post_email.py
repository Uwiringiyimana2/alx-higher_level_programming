#!/usr/bin/python3
import requests
import sys


payload = {'email': sys.argv[2]}
url = sys.argv[1]
r = requests.post(url, data=payload)
print("Your email is:", r.text)
