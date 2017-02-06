#!/usr/bin/env python
import requests

PYTHON_URL = "http://www.python.org"

response = requests.get(PYTHON_URL)
if response.status_code == requests.codes.ok:
    print("HEADERS:")
    for header_key, header_value in sorted(response.headers.items()):
        print("{:25s} {:50.50s}".format(header_key, header_value))
    print('-' * 60)
    print(response.content.decode())
else:
    print("Unable to get page:", response.status_code)
