#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)
"""
import urllib.parse
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    url_values = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, url_values)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
