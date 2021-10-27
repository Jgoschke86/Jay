#!/usr/bin/python3

import re

pat = re.compile("rabbit",re.I)

with open('../DATA/alice.txt') as alice_in:
    with open('badger.txt', 'w') as badger_out:
        for line in alice_in:
            line = pat.sub("badger",line)
            badger_out.write(line)

