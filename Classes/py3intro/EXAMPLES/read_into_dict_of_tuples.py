#!/usr/bin/python3
from pprint import pprint

knight_info = {}

with open("../DATA/knights.txt") as knights_in:
    for line in knights_in:
        (name, title, color, quest, comment) = line[:-1].split(":")
        knight_info[name] = title,color,quest,comment

print(knight_info)
print()
pprint(knight_info)
