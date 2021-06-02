print(29%26)
user_word = input("what do you want encrypted?  ")
user_cipher = input("what cipher do you want?   ")
abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
new_word = []
loc = []
new_loc = []
count = 0
s = ""

def split_word(word):
    return [char for char in word]

# def caesar(sent, place):
split_string = split_word(user_word)
shift = int(user_cipher)
for letter in split_string:
    if letter in abc:
        loc.append(abc.index(letter))
    else:
        loc.append(letter)
print(loc)
for i in loc:
    is_int = isinstance(i, int)
    if is_int == True:
        new_num = i + shift
        if new_num > 26:
            new_num = new_num % 26
    else:
        new_num = i
    new_loc.append(new_num)
print(new_loc)
for letter in split_string:
    if letter in abc:
        new_letter = abc[new_loc[count]]
        new_word.append(new_letter)
    else:
        new_word.append(letter)
    count += 1
print(new_word)

new_sent = s.join(new_word)
print(new_sent)
# cipher_message = caesar(user_word, user_cipher)


