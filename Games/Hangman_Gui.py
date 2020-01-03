from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title("Hangman")
root.config(bg = "blue")


guess0 = Image.open(file = r"C:\Users\jgoschke\Downloads\man0.gif")
man0 = ImageTk.PhotoImage(guess0)

dash_word = StringVar()
man_shape = StringVar()

dash_word.set("Test")
man_shape.set(man0)


word_box = Label(root, textvariable = dash_word, width = 30, height = 2)
word_box.config(font = 20, relief = SUNKEN)
word_box.grid(row = 1, column = 2, columnspan = 9)

a = Button(text = "A", width = 3, font = "bold").grid(row = 3, column = 1)
b = Button(text = "B", width = 3, font = "bold").grid(row = 3, column = 2)
c = Button(text = "C", width = 3, font = "bold").grid(row = 3, column = 3)
d = Button(text = "D", width = 3, font = "bold").grid(row = 3, column = 4)
e = Button(text = "E", width = 3, font = "bold").grid(row = 3, column = 5)
f = Button(text = "F", width = 3, font = "bold").grid(row = 3, column = 6)
g = Button(text = "G", width = 3, font = "bold").grid(row = 4, column = 1)
h = Button(text = "H", width = 3, font = "bold").grid(row = 4, column = 2)
i = Button(text = "I", width = 3, font = "bold").grid(row = 4, column = 3)
j = Button(text = "J", width = 3, font = "bold").grid(row = 4, column = 4)
k = Button(text = "K", width = 3, font = "bold").grid(row = 4, column = 5)
l = Button(text = "L", width = 3, font = "bold").grid(row = 4, column = 6)
m = Button(text = "M", width = 3, font = "bold").grid(row = 5, column = 1)
n = Button(text = "N", width = 3, font = "bold").grid(row = 5, column = 2)
o = Button(text = "O", width = 3, font = "bold").grid(row = 5, column = 3)
p = Button(text = "P", width = 3, font = "bold").grid(row = 5, column = 4)
q = Button(text = "Q", width = 3, font = "bold").grid(row = 5, column = 5)
r = Button(text = "R", width = 3, font = "bold").grid(row = 5, column = 6)
s = Button(text = "S", width = 3, font = "bold").grid(row = 6, column = 1)
t = Button(text = "T", width = 3, font = "bold").grid(row = 6, column = 2)
u = Button(text = "U", width = 3, font = "bold").grid(row = 6, column = 3)
v = Button(text = "V", width = 3, font = "bold").grid(row = 6, column = 4)
w = Button(text = "W", width = 3, font = "bold").grid(row = 6, column = 5)
x = Button(text = "X", width = 3, font = "bold").grid(row = 6, column = 6)
y = Button(text = "Y", width = 3, font = "bold").grid(row = 7, column = 3)
z = Button(text = "Z", width = 3, font = "bold").grid(row = 7, column = 4)

man_box = Label(root, image = man0, width = 15, height = 8, relief = SUNKEN)
man_box.image = man0
man_box.grid(row = 3, column = 8, rowspan = 4, columnspan = 4)

# Top row
blankbox1 = Label(root, height = 2, bg = "blue")
blankbox1.grid(row = 0, column = 0, columnspan = 4)
# Left side column
blankbox2 = Label(root, width = 2, bg = "blue")
blankbox2.grid(row = 1, column = 0, rowspan = 7)
# Center column
blankbox3 = Label(root, width = 2, bg = "blue")
blankbox3.grid(row = 2, column = 7, rowspan = 2)
# Right side column
blankbox4 = Label(root, width = 2, bg = "blue")
blankbox4.grid(row = 1, column = 13, rowspan = 7)
# Word and box spacer, row 3 spacer
blankbox5 = Label(root, height = 2, bg = "blue")
blankbox5.grid(row = 2, column = 1, columnspan = 6)
# Bottom row
blankbox6 = Label(root, height = 2, bg = "blue")
blankbox6.grid(row = 8, column = 1, columnspan = 4)

root.mainloop()