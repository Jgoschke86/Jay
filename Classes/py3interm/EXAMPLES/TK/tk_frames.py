#!/usr/bin/python3
from tkinter import *
top = Tk()

f_top = Frame(top)
tb1 = Button(f_top,text="A")
tb2 = Button(f_top,text="B")
tb3 = Button(f_top,text="C")

f_bottom = Frame(top)
bb1 = Button(f_bottom,text="X")
bb2 = Button(f_bottom,text="Y")
bb3 = Button(f_bottom,text="Z")

f_top.pack()
f_bottom.pack()

tb1.pack(side="left")
tb2.pack(side="left")
tb3.pack(side="left")

bb1.pack(side="left")
bb2.pack(side="left")
bb3.pack(side="left")

top.mainloop()
