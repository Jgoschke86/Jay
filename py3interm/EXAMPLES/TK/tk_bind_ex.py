#!/usr/bin/python3

from tkinter import *

def mk_callback(text_to_display):
    def tmp(w):
        lab.configure(text=text_to_display)
    return tmp

top = Tk()

lab = Label(top,text="Press Something...")
lab.pack()

b_quit = Button(top,text="Quit",command=top.destroy)
b_quit.pack()

top.bind("<a>",mk_callback("a"))
top.bind("<Control-a>",mk_callback("Ctrl-A"))
top.bind("<Alt-a>",mk_callback("Alt-A"))
top.bind("<Shift-A>",mk_callback("Shift-A"))

top.bind("<Escape>",mk_callback("Escape key"))
top.bind("<3>",mk_callback("right button"))

top.bind("<Unmap>",mk_callback("window back"))

top.mainloop()
