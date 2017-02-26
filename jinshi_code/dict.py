#!/usr/bin/env python
#Created by jinshiwu on 2/13/17.

dict = dict()
dict[2] = 'this'
dict[3] = "that"
dict['dd'] = 2

print(dict)
print(len(dict))
print(dict[3])

print('dd' in dict)
for  c in dict.items():
    print(c)

airports = { 'IAD':"Dulles",'RDU':"Raleigh-Durham",
             "DCA":"Reagan", "BWI":"Baltimore/Washington",
             "EWR":"Newark","ABQ":"Albuquerque",
             "GDB":"Granite Falls" ,
             }

print("""raw **************""")
print()

for abrv, airport in airports.items():
    print("{0:3s}, {1:<20s}".format(abrv, airport))

print("""sorted **************""")
print()

for abrv, airport in sorted(airports.items()):
    print("{0:3s}, {1:<20s}".format(abrv, airport))