#Basic Excercise
#Question 1 - return product and sum

# num1 = input("Please enter the first number: ")
# num2 = input("and the second number: ")

# product = int(num1) * int(num2)

# print("The product of the numers is " + str(product))

# if product > 1000:
#     add = int(num1) + int(num2)
#     print("The sum of the numbers is " + str(add))


#Question 2 - print sum of numbers through range

# num2 = 0

# for i in range(10):
#     num1 = i
#     if num1 >= 2:
#         num2 += 1
#     add = num1 + num2
#     print("Current number " + str(num1) + " Previous number " + str(num2) + " Sum " + str(add))


#Question 3 - print even indexed characters in word

# word = input("Please enter the word: ")

# num = 0
# letters = []
# for i in word:
#     letters.append(i)
# if len(letters) % 2 != 0:
#     length = (len(letters) - 1) / 2
# else:
#     length = len(letters) / 2

# print("Original string is " + word)
# print("Printing only even index characters")
# for j in range(int(length)):
#     print(letters[num])
#     num += 2


#Question 4 - remove j characters in word

# word = input("Please enter word: ")
# num = input("Please enter number: ")
# letters = []
# s = ""
# for i in word:
#     letters.append(i)
# if int(num) >= len(letters):
#     print("You entered a number that doesn't work. Please try again.")
# else:
#     for j in range(int(num)):
#         letters.pop(0)
#     joined_word = s.join(letters)
#     print(joined_word)


#Question 5 - same first and last number given in list

# num1 = input("Please enter 4 numbers: ")
# num2 = input()
# num3 = input()
# num4 = input()
# numbers = []
# numbers.append(num1)
# numbers.append(num2)
# numbers.append(num3)
# numbers.append(num4)
# first = numbers[0]
# last = numbers[-1]
# print("Give the list " + str(numbers))
# if first == last:
#     print("Result is True")
# else:
#     print("Result is False")


#Question 6 - list numbers divisible by 5

# num1 = input("Please give a number: ")
# num2 = input("Please give a number: ")
# num3 = input("Please give a number: ")
# num4 = input("Please give a number: ")
# numbers = []
# numbers.append(int(num1))
# numbers.append(int(num2))
# numbers.append(int(num3))
# numbers.append(int(num4))
# print("Divisible by 5 in list")
# for i in numbers:
#     if i % 5 == 0:
#         print(i)
#     else:
#         pass


#Question 7 - count times word appears in string

# word = input("What word would you like to count? ")
# sent = input("What is the sentence to search through? ")
# words = sent.split()
# times = 0
# for i in words:
#     if word.lower() == i.lower():
#         times += 1
# if times == 0:
#     print("Your word does not appear in the sentence.")
# else:
#     print("Your word appears " + str(times) + "times.")


#Question 8 - print pattern

# for num in range(10):
#     for i in range(num):
#         print(str(num), end = "")
#     print("\n")


#Question 9 - reverse number and see if it is the same

# number = input("What is your number? ")
# numbers = []
# final_number = ""
# for num in number:
#     numbers.append(num)
# numbers.reverse()
# final_number = final_number.join(numbers)
# if number == final_number:
#     print("The original and reversed number are the same.")
# else:
#     print("The original and reversed number are not the same.")

#Question 10 - combine lists

# first_list = [10, 20, 23, 11, 17]
# second_list = [13, 43, 24, 36, 12]
# result = []
# for num in first_list:
#     if num % 2 == 1:
#         result.append(num)
# for num in second_list:
#     if num % 2 == 0:
#         result.append(num)
# print(result)


#Question 11 - reverse and split num

# number = input("What is the number? ")
# numbers = []
# final = " "
# for num in number:
#     numbers.append(num)
# numbers.reverse()
# final = final.join(numbers)
# print(str(final))


#Question 12 - tax income

# income = int(input("What is your income? "))
# first = 0
# second = 0
# third = 0
# if income > 20000:
#     first = 10000
#     second = 10000
#     third = income - first - second
# elif income > 10000:
#     first = 10000
#     second = 10000
# else:
#     first = income
# taxable = (first * 0) + (second * .1) + (third * .2)
# print("Your taxes are " + str(taxable))


#Question 13 - multiplication table

# numbers = []
# for num in range(1,11):
#     for i in range(1,11):
#         print(num * i, end = " ")
#     print("\r")


#Question 14 - downward pyramid

# n = 5
# for i in range(n):
#     print("* " * n)
#     n -=1


#Question 15 - exponents

# base = int(input("What is the base number? "))
# exp = int(input("What is the power? "))
# num = pow(base, exp)
# print(num)


#Input Ouput
#Question 1 - 2 number multi

# num1 = int(input("What is your first number? "))
# num2 = int(input("What is your second number? "))
# multi = num1 * num2
# print("Your answer is " + str(multi))


#Question 2 - split and join name

# sent = "My name is James"
# words = sent.split()
# sent2 = "**"
# sent2 = sent2.join(words)
# print(sent2)


#Question 4 - rounding

# dis = 458.541315
# dis = round(dis, 2)
# print(dis)

#Question 5 - list input

# num = []
# for i in range(5):
#     num.append(float(input("Please give a number. ")))
# print(num)

#Question 7 - 3 strings

# str1, str2,str3 = input("Enter 3 strings ").split()
# print(str1, str2, str3)


#Question 8 - foramtting

# total_money = 1000
# quantity = 3
# price = 450
# print(f"I have {total_money} dollars so i can buy {quantity} tickets for {price} dollars.")



#Loops
#Question 1 - number loop

# num = 0
# while num <= 10:
#     print(num)
#     num += 1


 # Question 2 - pattern

# num = 6
# for i in range(1,num):
#     for j in range(1, i+1):
#         print(j, end= " ")
#     print(" ")



#Question 3 - sum of numbers

# num = int(input("What is your number? "))
# for i in range(1, num + 1):
#     print(num + i)


#Question 4 - multi table

# num = int(input("What is your number? "))

# for i in range(1, 11):
#     print(i * num)


#Question 5 - list iter

# list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

# for num in list1:
#     if num >= 150:
#         print(num)
#         break
#     elif num % 5 == 0:
#         print(num)
#     else:
#         pass


#Question 6 - number of digits in num

# num = input("What is your number? ")
# ind = []
# for x in num:
#     ind.append(x)
# print(len(ind))


#Question 7 - pattern

# n = 5
# for i in range(0, 5):
#     for j in range(n, 0, -1):
#         print(j, end = " ")
#     n -= 1
#     print("")


#Question 8 - reverse list

# list1 = [10, 20, 30, 40, 50]
# for i in range(4,-1,-1):
#     print(list1[i])


# Question 9 - numbers

# for num in range(-10, 0):
#     print(num)


# Question 10 - done

# for i in range(5):
#     print(i)
# print("Done")


# Question 11 - prime numbers

# print("Prime numbers between 25 and 50 are:")

# for num in range(25, 51):
#     for i in range(2, num):
#         if (num % i) == 0:
#             break
#     else:
#         print(num)


# Question 12 - Fibonacci

# fib = []
# num = 0
# while len(fib) != 10:
#     if num <= 1:
#         fib.append(num)
#         num += 1
#     else:
#         answer = fib[-1] + fib[-2]
#         fib.append(answer)
# print(fib)


# Question 13 - factorial

# def factor(num):
#     for i in range(1,num):
#         num = i * num
#     return num

# num = int(input("what is the number: "))
# print(factor(num))


# Question 14 - reverse number

# n = 4562
# rev = 0

# while(n > 0):
#     a = n % 10
#     rev = rev * 10 + a
#     n = n // 10

# print(rev)


# Question 15 - only even positions

# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# for num in my_list[1:len(my_list):2]:
#     print(num)


# Question 16 - cube number


# def cubed(a):
#      cubed = a *a *a
#      return cubed
# a = int(input("What number you want cubed?  "))
# print(cubed(a))


# Question 17 - sum of series

# terms = int(input("How many times would you like to repeat?  "))
# start = int(input("What number?  "))
# new_start = start
# sum = 0
# for i in range(terms):
#     print(new_start, end = " ")
#     sum += new_start
#     new_start = new_start * 10 + start
# print("\nThe sum of your sequence is ", sum)


# Question 18 - pattern

# star = "*"
# num = 0
# for i in range(1,6):
#     print(star * i)
# for i in range(4,0,-1):
#     print(star*i)


# Function Excercise
# Question 1 - name/age
# def info(name, age):
#     print(name, age)

# info("Bob", 23)

# Question 2 - var length arg
# def func1(*args):
#     for i in args:
#         print(i)
# func1(20,40,60)
# func1(80,100)

# Question 3 - calculation
# def calc(a,b):
#     add = a + b
#     sub = a - b
#     print(add,sub)
# calc(40, 10)

# Question 4 - employee
# def employ(name, sal = 9000):
#     print("Emplyee ", name, "salary is: ", sal)

# employ("Ben", 2000)
# employ("Ben")

# Question 5 - inner addition
# def outter(a,b):
#     def inner(a,b):
#         return a+b
#     add = inner(a,b)
#     return add+5

# res = outter(5,10)
# print(res)

# Question 6 - recursive
# def calculateSum(num):
#     if num:
#         return num + calculateSum(num-1)
#     else:
#         return 0

# res = calculateSum(10)
# print(res)

# Question 7 - assign new name

# def display_student(name, age):
#     print(name, age)

# display_student("Emma", 26)
# show_student = display_student
# show_student("Brad", 30)

# Question 8 - gen list
# print(list(range(4,30,2)))

# Question 9 - return largest item

# lista = [4,6,8,24,12,2]
# print(max(lista))


# Data Structure
# Question 1 - odd even list
# list_one = [3,6,9,12,15,18,21]
# list_two = [4,8,12,16,20,24,28]
# print("Element at odd-index positions from list one")
# list_one_odd = list_one[1::2]
# print(list_one_odd)
# print("Element at even-index positions from list two")
# list_two_even = list_two[0::2]
# print(list_two_even)
# print("Printing final third list")
# third = []
# third.extend(list_one_odd)
# third.extend(list_two_even)
# print(third)

# Question 2 - move stuff
# list_one = [34, 54, 67, 89, 11, 43, 94]
# print("Original list ", list_one)
# removed = list_one.pop(4)
# print(list_one)
# list_one.insert(2, removed)
# print(list_one)
# list_one.append(removed)
# print(list_one)

# Question 3 - slice list
og_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
list_length = len(og_list) / 3
first = 



