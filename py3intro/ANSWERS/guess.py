#!/usr/bin/python3

max = 26
min = 0
tries = 0

while True:
    guess = int((max + min)/2)
    ans = input("Is {0} your number? ".format(guess))

    if ans == "q":
        break

    tries = tries + 1

    if ans == "h":
        max = guess
    elif ans == "l":
        min = guess
    elif ans == "y":
        print("I got it in {0} tries!".format(tries))
        break
    else:
        print("Please enter h, l, or y")

