#!/usr/bin/python3

import sys
from tempconv import c2f

c = float(sys.argv[1])

f = c2f(c)

print("{0:.1f} C is {1:.1f} F".format(c,f))

