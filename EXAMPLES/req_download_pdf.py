#!/usr/bin/env python
import sys
import os
import requests

# url to download the requests documentation as a PDF file
# (the file is displayed after retrieval)

REQUESTS_DOCS_URL = 'http://readthedocs.org/projects/requests/downloads/pdf/master/'
REQUESTS_DOCS_FILENAME = 'requests_docs.pdf'

try:
    response = requests.get(REQUESTS_DOCS_URL)
except requests.HTTPError as err:
    print("Sorry,", err)
    exit(1)

if response.status_code == requests.codes.ok:

    with open(REQUESTS_DOCS_FILENAME, 'wb') as docs_out:
        docs_out.write(response.content)

    if sys.platform == 'win32':
        cmd = REQUESTS_DOCS_FILENAME
    elif sys.platform == 'darwin':
        cmd = 'open ' + REQUESTS_DOCS_FILENAME
    else:
        cmd = 'acroread ' + REQUESTS_DOCS_FILENAME

    os.system(cmd)

else:
    print("Unable to read document")
