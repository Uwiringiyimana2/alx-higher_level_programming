#!/usr/bin/python3
import requests
import sys
from requests.exceptions import HTTPError


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)

    try:
        r.raise_for_status()
        print(r.text)
    except HTTPError as e:
        print("Error code:", r.status_code)
