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