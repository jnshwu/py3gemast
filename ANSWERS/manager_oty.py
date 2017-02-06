#!/usr/bin/env python
"""

@author: jstrick
Created on Wed Mar 20 07:12:16 2013

"""
import csv
import zipfile
import requests

MASTER_URL = 'http://www.baseball-databank.org/files/tables/Master.zip'
AWARD_URL = 'http://www.baseball-databank.org/files/tables/AwardsManagers.zip'

def get_file_from_url(url,local_name):
    response = requests.get(url)
    with open(local_name, 'wb') as file_out:
        file_out.write(response.content)

def extract_file(zip_file_name, member_name):
    zipper = zipfile.ZipFile(zip_file_name)
    zipper.extract(member_name)

def make_name_lookup():
    info = {}
    with open('adminDB/Master.txt') as MASTER:
        master = csv.reader(MASTER)
        for row in master:
            if row[2]:
                info[row[2]] = (row[16],row[17])

    return info



get_file_from_url(MASTER_URL, 'Master.zip')
get_file_from_url(AWARD_URL, 'AwardsManager.zip')

extract_file('Master.zip', 'adminDB/Master.txt')
extract_file('AwardsManager.zip', 'adminDB/AwardsManagers.txt')

name_lookup = make_name_lookup()

with open('adminDB/AwardsManagers.txt') as AWARDS:
    awards = csv.reader(AWARDS)
    for row in awards:
        xref = row[0]
        year = row[2]
        league = row[3]
        name = ' '.join(name_lookup[xref])

        print("{0} {1} ({2})".format(year,name,league))

