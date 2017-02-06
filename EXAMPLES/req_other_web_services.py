#!/usr/bin/env python
# (c) 2016 John Strickler
#
import requests

print('PUT:')
r = requests.put("http://httpbin.org/put", data={'spam': 'ham'})
print(r.status_code, r.content.decode())
print('-' * 60)

print('DELETE:')
r = requests.delete("http://httpbin.org/delete")
print(r.status_code, r.content.decode())
print('-' * 60)

print('HEAD:')
r = requests.head("http://httpbin.org/get")
print(r.status_code, r.content.decode())
print(r.headers)
print('-' * 60)

print('OPTIONS:')
r = requests.options("http://httpbin.org/get")
print(r.status_code, r.content.decode())
print('-' * 60)
