#!/usr/bin/python3

import sys
import re

if len(sys.argv) < 3:
    print("Usage: pfind PATTERN file ...")
    sys.exit(1)

try:
    pat = re.compile(sys.argv[1])
except Exception as e:
    print("Error compiling RE: {0}".format(e))
    sys.exit()

for file_name in sys.argv[2:]:
    try:
        f = open(file_name)
    except IOError as e:
        print("Unable to open {0}: {1}".format(file_name,e))
        continue
    else:
        for line in f:
            if pat.search(line):
                print("{0}: {1}".format(file_name,line), end=' ')
        f.close()
    
