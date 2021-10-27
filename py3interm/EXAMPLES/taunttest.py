#!/usr/bin/python3

import sys
import taunt

print(taunt.taunt(4))
print("*" * 5)
for i in range(5):
    print(taunt.randtaunt())
print("*" * 5)
print("There are {0} taunts".format(taunt.tauntcount()))