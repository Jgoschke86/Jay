#!/usr/bin/env python

import urllib.request, urllib.error, urllib.parse

u = urllib.request.urlopen("http://www.google.com")

print(u.info())
print()

print(u.read(500).decode())
