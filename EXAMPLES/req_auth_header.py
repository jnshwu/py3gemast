#!/usr/bin/env python
import requests

# goes stale in 48 hours -- visit http://requestb.in to get a
# fresh URL
BASE_URL = 'http://requestb.in/xnfrvwxn'
AUTH_TOKEN = 'CJAssociatesTraining'
AUTH_KEY= 'MDowYzMxMTg5Mi0yMzA5LTExZTUtODcxMC0wNzEwNDcxM2NkOTA6QVBxNklDQXU1M2RSNEkyUjBBOEpkZVNQQVJUYXY2Q3liSzBy'

response = requests.get(
    BASE_URL,
    auth=(AUTH_TOKEN, AUTH_KEY)
)

print("response:", response.status_code)
