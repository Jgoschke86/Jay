#!/usr/bin/env python
# (c)2014 John Strickler
# 
import timeit

setup_code = 'values = []'

test_code_one = '''
for i in range(10000):
    values.append(i)
'''
test_code_two = '''
i = 0
while i < 10000:
    values.append(i)
    i += 1
'''

t1 = timeit.Timer(test_code_one, setup_code)
t2 = timeit.Timer(test_code_two, setup_code)

print("test one:")
print(t1.timeit(1000))
print()

print("test two:")
print(t2.timeit(1000))
print()
