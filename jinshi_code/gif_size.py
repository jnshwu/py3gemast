#!/usr/bin/env python
#Created by jinshiwu on 2/8/17.

from struct import unpack

with open('../DATA/salad.gif', 'rb') as gif_in:
    gif_info = gif_in.read(11)
    if gif_info[:3] == b'GIF':
        print('this is a gif file')
        height_bytes = gif_info[6:8]
        width_bytes = gif_info[8:10]
        height = unpack('h', height_bytes)
        width = unpack('h', width_bytes)
        print('gif size {0} x {1}'.format(width, height))