#!/usr/bin/python3

class Simple:
	def __init__(self, message):
		self._message = message

	def info(self):
		return self._message

if __name__ == "__main__":
	s = Simple('hello')
	print(s.info())

