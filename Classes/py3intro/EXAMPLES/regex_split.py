#!/usr/bin/python3

import re

rx_wordsep = re.compile(r"[\W']+")

s1 = 'There are 10 kinds of people in a Binary world -- "Geek talk"'

words = rx_wordsep.split(s1)
print(words)

