import random

# word_list = open(r"C:\Users\jgosc\Documents\GitHub\Jay\Games\Hangman\word_list.txt")
secret_word = random.choice(open(r"C:\Users\jgosc\Documents\GitHub\Jay\Games\Hangman\word_list.txt").readlines())

print(secret_word)
