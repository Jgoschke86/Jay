#!/usr/bin/python3

import operator

pres_names = [ ("George","","Washingon"), ("John","","Adams"),("John","Quincy","Adams"),("Franklin","Delano","Roosevelt"),("Richard","Milhous","Nixon"),
 ("James","","Monroe"),("James","","Madison") ]


print("sort by first name")
psort = sorted(pres_names)
for pres_name in psort:
    print(" ".join(pres_name))
print()

print("sort by last name")
psort = sorted(pres_names,key=operator.itemgetter(2,1))
for pres_name in psort:
    print(" ".join(pres_name))
print()
