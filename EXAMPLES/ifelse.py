#!/usr/bin/env python

raw_temp = input("Enter the temperature: ")
temp = int(raw_temp)
if temp < 76:
    print("Don't go swimming")

raw_num = input("Enter a number: ")
num = int(raw_num)

if num > 1000000:
    print(num, "is a big number")
else:
    print("your number is",num)

raw_hour = input("Enter the hour: ")
hour = int(raw_hour)

if hour < 12:
    print("Good morning")
elif hour < 18:
    print("Good afternoon")
elif hour < 23:
    print("Good evening")
else:
    print("You're up late")
