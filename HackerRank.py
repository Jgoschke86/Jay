

###Capitalize beggining letter of each word in a string
# capitalized_word_list = [word.capitalize() for word in s.split(' ')]
# return ' '.join(capitalized_word_list)

def swap_case(s):
    word = s.split()
    print(word)
    j = []
    for t in word:
        for u in t:
            j.append(u)
    print(j)
    for i in u:
        if i.isupper():
            i.lower()
        else:
            i.upper()
    return " ".join(j)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)