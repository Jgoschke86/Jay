#!/usr/bin/python3

with open("../DATA/mystery","rb") as m:
    d = m.read()[::2]  # get every other byte
    print((d.decode()))  # decode from bytes to printable string
