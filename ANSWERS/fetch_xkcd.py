#!/usr/bin/env python

import sys
import os
import requests

URL = 'http://imgs.xkcd.com/comics/python.png'
SAVED_FILENAME = 'xkcd.png'
DEFAULT_VIEWER = 'eog'

try:
    response = requests.get(URL)
except requests.HTTPError as e:
    print("Unable to open URL:", e)
    sys.exit(1)

with open(SAVED_FILENAME, 'wb') as xkcd_out:
    xkcd_out.write(response.content)

if sys.platform == 'win32':
    cmd = SAVED_FILENAME
elif sys.platform == 'darwin':
    cmd = 'open ' + SAVED_FILENAME
else:
    cmd = DEFAULT_VIEWER + ' ' + SAVED_FILENAME

os.system(cmd)
