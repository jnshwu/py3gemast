#!/usr/bin/env python

while True:
    c = input('Enter Celsius temp: ')
    if c.lower() == 'q':
        break

    try:
        c = float(c)
    except ValueError as e:
        print("Invalid number\n")
        continue

    f = ((9 * c) / 5 ) + 32
    print('{0:.1f} C is {1:.1f} F\n'.format(c,f))

