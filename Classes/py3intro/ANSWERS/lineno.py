#!/usr/bin/python3

import sys

for file_name in sys.argv[1:]:
    with open(file_name) as file_in:
        for i, line in enumerate(file_in,1):
            print("{0:4d}: {1}".format(i, line), end='')


