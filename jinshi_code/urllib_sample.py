#!/usr/bin/env python
#Created by jinshiwu on 2/4/17.

import urllib.request

x = urllib.request.urlopen('https://www.google.com/')
print(x.read())