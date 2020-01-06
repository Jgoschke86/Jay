from tkinter import *
from random import choice



root = Tk()
root.title("Hangman")
root.config(bg = "blue")
secret_word = ""


wrong_guess_count = 0
letter = []
dash_letter = []
guessed_letter = []
dash_word = StringVar()
man_shape = StringVar()
selected_letter = ""

# Command to open txt file, select a random word, convert it to dashes to disply in word_box
def pick_word():
    secret_word = choice(open(r"C:\Users\jgosc\Documents\GitHub\Jay\Games\Hangman\word_list.txt").readlines())
    for x in secret_word:
        letter.append(x)
    for i in letter:
        dash_letter.append("_")
    dashed_word  = (" ".join(map(str, dash_letter)))
    dash_word.set(dashed_word)
def correct_letter(evt):
    while True:
        if selected_letter in letter:
            correct = letter.index(selected_letter)
            dashed_word[correct] = selected_letter        #Converts dash to letter
            letter[correct] = "@"               #Converts letter in "letter list" to @
            guessed_letter.append(selected_letter)#Adds letter to list
            guessed_letter.sort()
            
        else:
            
            break


def wrong_letter(evt):
    pass        

def l_a():
    selected_letter = "a"
    correct_letter
    dash_word.set(dashed_word)
def l_b(evt):
    pass
def l_c(evt):
    pass
def l_d(evt):
    pass
def l_e(evt):
    pass
def l_f(evt):
    pass
def l_g(evt):
    pass
def l_h(evt):
    pass
def l_i(evt):
    pass
def l_j(evt):
    pass
def l_k(evt):
    pass
def l_l(evt):
    pass
def l_m(evt):
    pass
def l_n(evt):
    pass
def l_o(evt):
    pass
def l_p(evt):
    pass
def l_q(evt):
    pass
def l_r(evt):
    pass
def l_s(evt):
    pass
def l_t(evt):
    pass
def l_u(evt):
    pass
def l_v(evt):
    pass
def l_w(evt):
    pass
def l_x(evt):
    pass
def l_y(evt):
    pass
def l_z(evt):
    pass
# Menu bar details
menu_bar = Menu(root)
file = Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = "File", menu = file)
file.add_command(label = "New Word", command = pick_word)
file.add_command(command = root.destroy, label = "Exit")




man_shape.set("test")


# Label for displaying randomly selected word to guess
word_box = Label(root, textvariable = dash_word, width = 30, height = 2, font=("bold", 13), relief = SUNKEN)
word_box.config(anchor = S)
word_box.grid(row = 1, column = 2, columnspan = 9)


# Buttons for letter guessing
a = Button(text = "A", width = 3, font = "bold", command = l_a).grid(row = 3, column = 1)
b = Button(text = "B", width = 3, font = "bold", command = l_b).grid(row = 3, column = 2)
c = Button(text = "C", width = 3, font = "bold", command = l_c).grid(row = 3, column = 3)
d = Button(text = "D", width = 3, font = "bold", command = l_d).grid(row = 3, column = 4)
e = Button(text = "E", width = 3, font = "bold", command = l_e).grid(row = 3, column = 5)
f = Button(text = "F", width = 3, font = "bold", command = l_f).grid(row = 3, column = 6)
g = Button(text = "G", width = 3, font = "bold", command = l_g).grid(row = 4, column = 1)
h = Button(text = "H", width = 3, font = "bold", command = l_h).grid(row = 4, column = 2)
i = Button(text = "I", width = 3, font = "bold", command = l_i).grid(row = 4, column = 3)
j = Button(text = "J", width = 3, font = "bold", command = l_j).grid(row = 4, column = 4)
k = Button(text = "K", width = 3, font = "bold", command = l_k).grid(row = 4, column = 5)
l = Button(text = "L", width = 3, font = "bold", command = l_l).grid(row = 4, column = 6)
m = Button(text = "M", width = 3, font = "bold", command = l_m).grid(row = 5, column = 1)
n = Button(text = "N", width = 3, font = "bold", command = l_n).grid(row = 5, column = 2)
o = Button(text = "O", width = 3, font = "bold", command = l_o).grid(row = 5, column = 3)
p = Button(text = "P", width = 3, font = "bold", command = l_p).grid(row = 5, column = 4)
q = Button(text = "Q", width = 3, font = "bold", command = l_q).grid(row = 5, column = 5)
r = Button(text = "R", width = 3, font = "bold", command = l_r).grid(row = 5, column = 6)
s = Button(text = "S", width = 3, font = "bold", command = l_s).grid(row = 6, column = 1)
t = Button(text = "T", width = 3, font = "bold", command = l_t).grid(row = 6, column = 2)
u = Button(text = "U", width = 3, font = "bold", command = l_u).grid(row = 6, column = 3)
v = Button(text = "V", width = 3, font = "bold", command = l_v).grid(row = 6, column = 4)
w = Button(text = "W", width = 3, font = "bold", command = l_w).grid(row = 6, column = 5)
x = Button(text = "X", width = 3, font = "bold", command = l_x).grid(row = 6, column = 6)
y = Button(text = "Y", width = 3, font = "bold", command = l_y).grid(row = 7, column = 3)
z = Button(text = "Z", width = 3, font = "bold", command = l_z).grid(row = 7, column = 4)


man_box = Label(root, width = 20, height = 10, relief = SUNKEN)
man_box.grid(row = 3, column = 8, rowspan = 4, columnspan = 4)


# Empty boxes for spacing
# Top row
blankbox1 = Label(root, height = 2, bg = "green")
blankbox1.grid(row = 0, column = 0, columnspan = 4)
# Left side column
blankbox2 = Label(root, width = 2, bg = "pink")
blankbox2.grid(row = 1, column = 0, rowspan = 7)
# Center column
blankbox3 = Label(root, width = 2, bg = "red")
blankbox3.grid(row = 2, column = 7, rowspan = 2)
# Right side column
blankbox4 = Label(root, width = 2, bg = "orange")
blankbox4.grid(row = 1, column = 13, rowspan = 7)
# Word and box spacer, row 3 spacer
blankbox5 = Label(root, height = 2, bg = "yellow")
blankbox5.grid(row = 2, column = 1, columnspan = 6)
# Bottom row
blankbox6 = Label(root, height = 2, bg = "blue")
blankbox6.grid(row = 8, column = 1, columnspan = 4)


root.config(menu = menu_bar)
root.mainloop()