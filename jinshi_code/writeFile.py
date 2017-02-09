#!/usr/bin/env python
#Created by jinshiwu on 2/7/17.

states = ['ohio', 'wisconsin', 'north carolina']
fruits = [ 'apple', 'cherry', 'peach', 'lemon', 'banana']

with open('state.txt', 'w') as state_out:
    for state in states:
        state_out.write(state + '\n')
    for fruit in fruits:
        state_out.write(fruit + "\n")