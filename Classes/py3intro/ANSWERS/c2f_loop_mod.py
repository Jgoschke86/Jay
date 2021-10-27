#!/usr/bin/python3

from tempconv import c2f

while True:
    user_input = input('Enter Celsius temp: ')
    if user_input.lower() == 'q':
        break
    if user_input == '':
        continue
    celsius = float(user_input)
    fahrenheit = c2f(celsius)
    print('{0:.1f} C is {1:.1f} F\n'.format(celsius, fahrenheit))
