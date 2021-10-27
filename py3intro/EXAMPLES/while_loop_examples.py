#!/usr/bin/python3

while True:
	name = input("Enter a name (or q to quit): ")
	if name.lower() == 'q':
		print("goodbye!")
		break
	print("welcome, ",name)
