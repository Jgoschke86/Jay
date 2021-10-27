#!/usr/bin/python3

def c2f(celsius):
    celsius = float(celsius)
    fahrenheit = ((9 * celsius) / 5 ) + 32

    return fahrenheit

while True:
	raw_celsius = input('Enter Celsius temp: ')
	if raw_celsius.lower().startswith('q'):
		break
	celsius = float(raw_celsius)
	fahrenheit = c2f(celsius)
	print('{0:.1f} C is {1:.1f} F\n'.format(celsius, fahrenheit))

