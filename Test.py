from random import randint

word_list = open(file = r"C:\Users\jgosc\Documents\GitHub\Jay\Games\Hangman\word_list.txt")
secret_word = word_list.readlines(20)

print(secret_word)
word_list.close()