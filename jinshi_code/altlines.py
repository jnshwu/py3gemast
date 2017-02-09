#!/usr/bin/env python
#Created by jinshiwu on 2/8/17.

with open('../DATA/alt.txt') as alt_in:
    with open('a.txt', 'w') as a_out:
        with open('b.txt', 'w') as b_out:
            for line in alt_in:
                if line.lower().startswith('a'):
                    a_out.write(line)
                elif line.lower().startswith('b'):
                    b_out.write(line)
                else:
                    continue