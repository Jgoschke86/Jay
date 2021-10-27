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
    for color in ('red','yellow','green','blue','purple','grey','pink','brown',
        'lavender','mauve','brown','white','black','navy','salmon','scarlet'):
        display_area.insert('end',color + "\n")

top = Tk()
top.title("Fun with Text Entry")

f_disparea = Frame(top)
f_disparea.pack()

display_area = Text(f_disparea,height=8,width=50) # size in chars
display_area.pack(side=LEFT)

scroll = Scrollbar(f_disparea)
scroll.pack(side=LEFT,fill=Y)

display_area.configure(yscrollcommand = scroll.set)
scroll.configure(command=display_area.yview)


b_animals = Button(top,text="Fill with animals",command=fill_with_animals)
b_animals.pack()

b_colors = Button(top,text="Fill with colors",command=fill_with_colors)
b_colors.pack()

b_quit = Button(top,text="Quit",command=top.destroy)
b_quit.pack()

fill_with_animals()  # default 

top.mainloop()

