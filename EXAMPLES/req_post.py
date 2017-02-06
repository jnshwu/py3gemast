#!/usr/bin/env python
# (c)2015 John Strickler

import requests
import datetime as dt
import time

# note: go to http://requestb.in/ and create a new RequestBin -- put the URL here:
#   then go to http://requestb.in/, select the bin, and view the results

URL = 'http://requestb.in/xnfrvwxn'  # ephemeral -- goes stale in 48 hours or so

for i in range(5):
    response = requests.post(
        URL,
        data={'date': dt.datetime.now(),
              'label': 'test_' + str(i)
              }

    )
    time.sleep(1)

    print(response.status_code)
    print(response.content.decode())
    print('-' * 20)

