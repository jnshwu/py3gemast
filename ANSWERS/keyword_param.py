#!/usr/bin/env python
#Created by jinshiwu on 2/17/17.

def key_word(**whatever):
    for key, value in sorted(whatever.items()):
        print(key, value)

key_word(hello='this', jinshi='jinshi', say='how are you')


def spam(p1, p2, *p3, p4=None, **p5):
    print("p1:", p1)
    print("p2:", p2)
    print("p3:", p3)
    print("p4:", p4)
    print("p5:", p5)
    print()
spam('a', 'b')
spam('a', 'b', 'c', 'd', 'e')
spam('a', 'b', 'c', 'd', 'e', p4='f')
spam('a', 'b', 'c', 'd', 'e', ham='f', eggs='g')
spam('a', 'b', 'c', 'd', 'e', p4='f', ham='g', eggs='h')
spam('a', 'b', ham='g', eggs='h')
spam('a', 'b', 'c', ham='g', eggs='h')
spam('a', 'b', 'c', 'd', p4='e')