#!/usr/bin/python3

from tkinter import *
top = Tk()
add_cocoa = StringVar(top)
add_sugar = StringVar(top)
add_nutmeg = StringVar(top)
c1 = Checkbutton(top,text="Cocoa",variable=add_cocoa,)
c2 = Checkbutton(top,text="Sugar",variable=add_sugar)
c3 = Checkbutton(top,text="Nutmeg",variable=add_nutmeg)
c1.deselect()
c2.deselect()
c3.deselect()



dairy = StringVar(top)
r1 = Radiobutton(top,text="Whole Milk",
   value='milk',variable=dairy)
r1.select()
r2 = Radiobutton(top,text="Half-and-Half",
   value='half',variable=dairy)
r3 = Radiobutton(top,text="Skim Milk",
   value='skim',variable=dairy)
r4 = Radiobutton(top,text="2% Milk",
   value='twop',variable=dairy)
for w in (c1,c2,c3,r1,r2,r3,r4):
    w.pack(anchor='w')

b_quit = Button(top,text="Quit",command=top.destroy)
b_quit.pack()

top.mainloop()
