print(29%26)
user_word = input("what do you want encrypted?  ")
user_cipher = input("what cipher do you want?   ")
abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
new_word = []
is_cap = []
loc = []
new_loc = []
s = ""

def split_word(word):
    return [char for char in word]

split_string = split_word(user_word)
shift = int(user_cipher)

#  Converts letters to numerical location in alphabet
for letter in split_string:
    if letter.lower() in abc:
        loc.append(abc.index(letter.lower()))
    else:
        loc.append(letter)
    

#  Converts to new alphabet location
for i in loc:
    is_int = isinstance(i, int)
    if is_int == True:
        new_num = i + shift
        if new_num > 26:
            new_num = new_num % 26
    else:
        new_num = i
    new_loc.append(new_num)

#  Converts new location to letters
for num in new_loc:
    is_int = isinstance(num, int)
    if is_int == True:
        new_letter = abc[num]
        new_word.append(new_letter)
    else:
        new_word.append(num)

#  Joins letters to make new sentence
new_sent = s.join(new_word)
print(new_sent)



