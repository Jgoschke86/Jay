#!/usr/bin/python3

f = open("../DATA/tyger.txt","r")
for line in f:
	print(line[:-1])
f.close()
