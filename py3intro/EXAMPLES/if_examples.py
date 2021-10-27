#!/usr/bin/python3

temp = int(input("Enter the temperature: "))
if temp < 76:
    print("Don't go swimming")

num = int(input("Enter a number: "))
if num > 1000000:
	print(num,"is a big number")
else:
	print("your number is",num)

hour = int(input("Enter the hour: "))
if hour < 12:
	print("Good morning")
elif hour < 18:
	print("Good afternoon")
elif hour < 23:
	print("Good evening")
else:
	print("You're up late")
