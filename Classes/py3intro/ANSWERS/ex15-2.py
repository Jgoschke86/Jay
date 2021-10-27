#!/usr/bin/Python3

count_for = {}
with open('../DATA/presidents.txt') as PRES:
    for line in PRES:
        state = line.split(':')[10]  # state is 10th field on line
        count_for[state] = count_for.get(state,0) + 1

for state,count in sorted(count_for.items()):
    print(state,count)