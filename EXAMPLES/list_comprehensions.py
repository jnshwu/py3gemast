#!/usr/bin/env python

fruits = ['watermelon', 'apple', 'mango', 'kiwi', 'apricot', 'lemon', 'guava']

ufruits = [ fruit.upper() for fruit in fruits ]
afruits = [ fruit.title() for fruit in fruits if fruit.startswith('a') ]

print("ufruits:", " ".join(ufruits))
print("afruits:", " ".join(afruits))
print()

values = [ 2, 42, 18, 92, "boom", ['a','b','c'] ]
doubles = [ v * 2 for v in values ]

print("doubles:", end=' ')
for d in doubles:
    print(d, end=' ')
print("\n")

nums = [ int(s) for s in values if isinstance(s,int) ]
for n in nums:
    print(n, end=' ')
print("\n")

dirty_strings = [ '   Gronk    ','PULABA       ','        floog' ]

clean = [ d.strip().lower() for d in dirty_strings ]
for c in clean:
    print(">{0}<".format(c), end=' ')
print("\n")

powers = [ (i,i**2,i**3) for i in range(1,11) ]
for num,square,cube in powers:
    print("{0:2d} {1:3d} {2:4d}".format(num,square,cube))
print()

suits = 'Clubs','Diamonds','Hearts','Spades'
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

deck = [ (rank,suit) for suit in suits for rank in ranks ]

for rank,suit in deck:
    print("{0}-{1}".format(rank,suit))
