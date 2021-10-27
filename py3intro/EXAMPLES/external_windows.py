#!/usr/bin/env python

import os 

os.system(r"dir ..\DATA") 
print()

with os.popen("netstat -an") as NS: 
    for entry in NS:
        if 'ESTABLISHED' in entry:
            print(entry[:-1])
    print()

# backticks equivalent 
host_name = os.popen("hostname").read()

print(host_name)
