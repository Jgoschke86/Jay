#!/usr/bin/python3

spam = "spam"

def fun_one():
	print("Hello, world")

def fun_two(n):
	return n ** 2

def fun_three(n, *opt):
	print("n is ", n)
	print("opt is", opt)

def fun_four(**named_args):
	for name, value in named_args.items():
		print(name,"==> ", value)

def fun_five(count=3):
	for i in range(count):
		print(spam, end=' ')
	print()


fun_one()
x = fun_two(5)
print("fun_two(5) is", x)
fun_three('apple', "blueberry", "peach", "cherry")
fun_four(name="Lancelot", quest="Grail", color="red")
fun_five()
fun_five(5)
