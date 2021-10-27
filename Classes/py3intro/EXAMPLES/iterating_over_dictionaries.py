#!/usr/bin/python3

airports = { 'IAD':"Dulles",'RDU':"Raleigh-Durham",
	"DCA":"Reagan", "BWI":"Baltimore/Washington",
	"EWR":"Newark","ABQ":"Albuquerque",
	"GDB":"Granite Falls" }

print("*** raw")
for abbr, airport in airports.items():
	print("{0:3s} {1:<20s}".format(abbr,airport))

print()
print("*** sorted (unpacked tuple)")
for abbr, airport in sorted(airports.items()):
	print("{0:3s} {1:<20s}".format(abbr,airport))

print()
print("*** sorted (tuple only)")
for kv in sorted(airports.items()):
	print("{0[0]:3s} {0[1]:<20s}".format(kv))

