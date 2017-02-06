#!/usr/bin/env python
#Created by jinshiwu on 2/4/17.

max_number = int(input("please input max number"))
min_number = int(input("please input min number"))

number = int(input("please input secrect number"))

while True:
    guess = str(input("please input guess number"))
    if guess.lower() == 'q':
        break
    else:
        guess = int(guess)
        if guess > max_number or guess < min_number:
            print(guess, " out of range ", min_number, max_number)
        elif guess < max_number and guess > min_number:
            if guess > number:
                print("lower")
            elif guess < number:
                print("higher")
            else:
                print("bingo")
                break