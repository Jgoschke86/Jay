#!/usr/bin/python3

from tkinter import *

def clear_disp():
    display_area.delete('1.0','end')    # clear entire window

def fill_with_animals():
    clear_disp()
    for animal in ('lion','bear','giraffe','lemur','orangutan','elk', 'snail darter','vole','african swallow'):
        display_area.insert('end',animal + "\n")
        

def fill_with_colors():
    clear_disp()
    for color in ('red','yellow','green','blue','purple','grey','pink','brown'):
        display_area.insert('end',color + "\n")

mw = Tk()
mw.title("Fun with Text Entry")

display_area = Text(mw,height=8,width=50) # size in chars
display_area.pack()

b_animals = Button(mw,text="Fill with animals",command=fill_with_animals)
b_animals.pack()

b_colors = Button(mw,text="Fill with colors",command=fill_with_colors)
b_colors.pack()

b_quit = Button(mw,text="Quit",command=mw.destroy)
b_quit.pack()

fill_with_animals()  # default 
mw.mainloop()

