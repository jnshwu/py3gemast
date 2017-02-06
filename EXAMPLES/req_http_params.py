#!/usr/bin/env python
import requests

# goes stale in 48 hours -- visit http://requestb.in to get a
# fresh URL
REQUESTBIN_URL = 'http://requestb.in/xnfrvwxn'

HTTPBIN_URL = 'https://httpbin.org/get'

for url in REQUESTBIN_URL, HTTPBIN_URL:
    response = requests.get(
        url,
        params = {
            'color': 'deep purple',
            'language': 'Python',
            'state': 'Wisconsin',
        }
    )
    print(url)
    print("response:", response.status_code)
    print(response.content.decode())
    print()
